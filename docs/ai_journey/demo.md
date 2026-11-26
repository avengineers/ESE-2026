# The live demo of „Frag doch den Agenten!"

The talk opens with a live demo. On the user story slide, Judith starts an agent with the
prompt on the slide. The agent takes the story DEMO-002 "Auto Off" through the closed loop
while the speakers give the talk. On the slide "Die Abnahme", the speakers check the result.

This file says what to do before the talk, on stage and after the talk, and what to show
from where. The demo repository is
[xxthunder/asf-closed-loop-demo](https://github.com/xxthunder/asf-closed-loop-demo).

## The setup

The demo runs on one laptop: Windows with WSL.

| What | Where |
|---|---|
| The agent | Claude Code in a WSL terminal, started in the Kasten, auto mode |
| The demo checkout | `~/dev/xxthunder/asf-closed-loop-demo` in WSL |
| Its dev container | `asf-closed-loop-demo`, reached with `ssh asf-closed-loop-demo.devpod` |
| The worktree of the run | `.worktrees/demo-002` in the demo checkout, made by the agent |
| The Windows checkout for the UAT | `C:\dev\xxthunder\asf-closed-loop-demo` |
| The slides | this deck in a browser |

## Reset the demo

Run these steps before the talk and after every run. They put the demo repository back to
the tag `demo-start`, and build every variant and its report for the comparison. Open this
file on GitHub: each block has a copy button.

**Caution:** step 1 closes every open pull request of the demo repository, deletes every
remote branch except `develop`, and force-pushes `develop` to `demo-start`.

1. Paste this block into a WSL terminal. It takes about 3 minutes.

   ```bash
   (
     set -e
     cd ~/dev/xxthunder/asf-closed-loop-demo
     echo "== Close the open pull requests"
     gh pr list --state open --json number --jq '.[].number' | xargs -r -n1 gh pr close
     echo "== Delete every remote branch except develop"
     git fetch --prune --tags --force origin
     git for-each-ref --format='%(refname:lstrip=3)' refs/remotes/origin \
       | grep -v -x -e develop -e HEAD | xargs -r -n1 git push origin --delete
     echo "== Remove the worktrees and the local branches in the dev container"
     ssh asf-closed-loop-demo.devpod 'cd /workspaces/asf-closed-loop-demo \
       && for w in .worktrees/*/; do [ -d "$w" ] && git worktree remove --force "$w"; done; \
       git worktree prune && git checkout -q develop \
       && git branch --format="%(refname:short)" | grep -v -x develop | xargs -r git branch -D'
     echo "== Put develop back to demo-start"
     git checkout -q develop
     git reset -q --hard demo-start
     git push --force-with-lease origin develop
     echo "== Build every variant and its report in the dev container"
     ssh asf-closed-loop-demo.devpod 'cd /workspaces/asf-closed-loop-demo && scripts/gate'
     echo "== Done: develop is at $(git rev-parse --short HEAD), demo-start is at $(git rev-parse --short demo-start)"
   )
   ```

2. Check the last line. It must name the same commit twice.
3. If the board of the Kasten has a DEMO-002 card, say to the agent: "drop DEMO-002 from
   the board".
4. Paste this block into PowerShell, with the proxy set. It builds every variant on
   Windows, Sleep included.

   ```powershell
   & {
     Set-Location C:\dev\xxthunder\asf-closed-loop-demo
     Write-Host "== Put develop on demo-start and delete every other local branch"
     git fetch --prune --tags --force origin
     git switch -q -C develop demo-start
     git worktree prune
     git branch --format='%(if)%(worktreepath)%(then)%(else)%(refname:short)%(end)' | Where-Object { $_ -and $_ -ne 'develop' } | ForEach-Object { git branch -D $_ }
     Write-Host "== Build every variant and its report"
     .\build.ps1 -install
     .\build.ps1 -selftests -marker gate_develop_pr
     Write-Host "== Worktrees left:"
     git worktree list
     Write-Host "== Done: develop is at $(git rev-parse --short HEAD), demo-start is at $(git rev-parse --short demo-start)"
   }
   ```

5. Check the last line. It must name the same commit twice.
6. Check the list of worktrees. If it shows a worktree of an earlier DEMO-002 run, remove
   it by hand: it holds an old Auto Off.

The Sleep report of the start state is then at:

```text
\\wsl.localhost\deb-dev\home\wsluser\dev\xxthunder\asf-closed-loop-demo\build\Sleep\test\Debug\reports\html\index.html
```

## The day before

1. Update the Kasten, the Claude Code marketplaces and the plugins.
2. [Reset the demo](#reset-the-demo).
3. Do a full rehearsal run, with the steps of this file and the prompt from the slide.
4. Do not update anything after the rehearsal.

## One hour before the talk

**Caution:** the agent must not find an old solution on this laptop. Reset the demo before
you start Claude Code.

1. [Reset the demo](#reset-the-demo).
2. Check the start state. All of these must hold:
   - `gh pr list -R xxthunder/asf-closed-loop-demo` shows no open pull request.
   - DEMO-002 is *Open*, and the board has no DEMO-002 card.
3. Make sure that the proxy is up, the laptop is on power, and Windows shows no
   notifications.
4. Open the windows of the demo:
   - the deck, on the title slide;
   - a WSL terminal with Claude Code started in the Kasten, in auto mode, empty;
   - a browser tab with
     [the pull requests of the demo repository](https://github.com/xxthunder/asf-closed-loop-demo/pulls);
   - a browser tab with the Sleep report of the start state, for the comparison;
   - PowerShell in the Windows checkout.

## On stage

| When | Who | What | Where |
|---|---|---|---|
| User story slide | Judith | Copy the prompt with the copy button, paste it, send it. Go back to the deck. | deck, terminal |
| During the talk | both | Give the talk. Do not touch the session. | deck |
| A permission prompt appears | Judith | Allow it once. Say why it asks. | terminal |
| Slide "Die Abnahme" | Judith | Switch to the result. Show each check. | see below |
| After the verdict | Karsten | Next slide: "Fazit". | deck |

Expected times after the prompt, from the runs 3 and 4: the first Sleep report after 19 to
31 minutes, the pull request after 29 to 37 minutes, its CI green about 3 minutes later.

### What Judith shows on "Die Abnahme"

| Check on the slide | What to show | From where |
|---|---|---|
| UAT | The light goes off without input. | Windows, see below |
| Anforderungen ↔ SWDD | The design document of the new component: its specs refine REQ_39, REQ_40 and REQ_59. | The pull request, *Files changed*: `components/<new component>/doc/index.md` |
| SWDD ↔ Code | The `.. impl::` block in the doc comment of the function, with `:implements:`. | The pull request, *Files changed*: `components/<new component>/src/` |
| SWDD ↔ Tests | The `.. test::` blocks of the unit tests, with `:tests:`. | The pull request, *Files changed*: `components/<new component>/test/` |
| Tests ↔ Testergebnisse | The Sleep report: unit test results, coverage, traceability matrix. Compare it with the report of the start state. | The report on disk, see below |

Also show the pull request itself: its commits, the evidence package in its description,
and the green checks. They show how the agent got to the result.

**The UAT on Windows.** In PowerShell, in the Windows checkout:

1. Get the branch of the pull request. Its name is in the pull request.

   ```text
   git fetch origin
   git checkout <branch of the pull request>
   ```

2. Build Sleep:

   ```text
   .\build.ps1 -install
   .\build.ps1 -build -variants Sleep
   ```

3. Start the program: `.\build\Sleep\prod\Debug\spled.exe`.
4. Press `P`. The light goes on.
5. Wait without input. The light goes off.

**Caution:** on Windows, the light goes off after about 16 seconds, not 10. One task cycle
takes about 16 ms on Windows instead of 10 ms. The cause is older than the demo. Say it
before the audience counts.

**The report on disk.** Open this file in the browser:

```text
\\wsl.localhost\deb-dev\home\wsluser\dev\xxthunder\asf-closed-loop-demo\.worktrees\demo-002\build\Sleep\test\Debug\reports\html\index.html
```

The file exists only after the agent built the Sleep report in the worktree.

**When the agent is not finished.** Show what is ready: the task list in the session, the
commits in the worktree, a report if there is one. Or show the result of the rehearsal. Say
what you show.

## After the talk

1. [Reset the demo](#reset-the-demo). It closes the pull request of the run without a merge.

## Open

- Whether the prompt on the slide, "Packe DEMO-002 in die Loop! Energie!", starts the loop.
  The closed-loop skill lists "Nimm … in die Loop" and "Bring … in den Loop" as its
  phrases, not "Packe". The rehearsal must use the prompt from the slide.
- Where the rehearsal result is kept for the fallback. It must not be within reach of the
  agent: a run already found a checkout of the old solution on the same laptop.
- Whether VS Code shows the worktree live, connected to the dev container on the main
  checkout. Try it in a rehearsal first.
