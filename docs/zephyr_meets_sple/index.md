## There Is More to a Product Line Than Zephyr Boards

Asking the SPLE Question First

<hr>

ESE Kongress 2026 in Sindelfingen <!-- .element: class="ese-event" -->

<div class="ese-logos">
<img src="../images/RMT-Logo_TransparentBG.png" alt="RMT logo">
<img src="../images/Marquardt-100-Years-Keyvisual-white-gold.png" alt="Marquardt logo">
</div>

Note:

Welcome the audience. Say the title of the talk.

---

### Who am I?

<div class="speakers">
<div class="speaker">

![Alexandru](../images/alexandru.png)

Alexandru

</div>
</div>

Note:

Each speaker says who they are in one or two sentences.

---

<!-- .slide: data-background-color="#008080" -->

<div class="ie">
<div class="ie-title"><span>🌐 Alexandru Maxiniuc - Homepage - Microsoft Internet Explorer</span><span class="ie-ctl"><b>_</b><b>□</b><b>✕</b></span></div>
<div class="ie-menu"><span><u>F</u>ile</span><span><u>E</u>dit</span><span><u>V</u>iew</span><span>F<u>a</u>vorites</span><span><u>T</u>ools</span><span><u>H</u>elp</span></div>
<div class="ie-tools"><span>◀ Back</span><span>▶</span><span>✖ Stop</span><span>⟳ Refresh</span><span>⌂ Home</span><span>🔍 Search</span><span>★ Favorites</span></div>
<div class="ie-addr"><span>A<u>d</u>dress</span><span class="ie-url">http://www.maxiniuc.com/</span><span class="ie-go">➜ Go</span></div>
<div class="ie-page">
<marquee scrollamount="6">*** Welcome to my homepage!!! *** Thank you for visiting *** Please sign my guestbook ***</marquee>
<div class="ie-name">Alexandru Maxiniuc</div>
<p>I am interested in engineering software product lines, software architecture and build systems.</p>
<div class="ie-new"><span class="ie-blink">NEW!</span> Updated for the ESE Kongress 2026</div>
<div class="ie-uc">UNDER CONSTRUCTION</div>
<p class="ie-links"><a>[ About me ]</a> <a>[ My projects ]</a> <a>[ Guestbook ]</a> <a>[ Links ]</a> <a>[ Webring ]</a></p>
<div class="ie-counter">You are visitor number <span>000042</span></div>
<p class="ie-best">Best viewed with Internet Explorer 5.0 at 800x600</p>
</div>
<div class="ie-status"><span>Done</span><span>🌐 Internet</span></div>
</div>

Note:

The old homepage, "updated for the conference". The sentence on the page is from the About page of maxiniuc.com.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="now">Two customers, one product line</li>
<li>From wishes to features</li>
<li>A prototype on Zephyr</li>
<li>The series project starts</li>
<li>What it really takes</li>
<li>A better way</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>We follow one product line from the first customer e&#8209;mail to the series product.</p>
<p>Along the way, we collect what the development environment needs.</p>
</div>
</div>

Note:

The common thread, not an agenda: one product line, from the e-mail to series production, and the requirements we find on the way.

---

<p class="label">// context</p>

<div class="stage">
<div class="lead abs" style="left:0; top:0; width:880px;">We are a supplier. We build SPLed, a small light controller, for two customers.</div>
<div class="customer abs" style="left:80px; top:220px;">Customer A</div>
<div class="customer abs" style="left:500px; top:220px;">Customer B</div>
<div class="wall abs fragment" style="left:438px; top:200px;"></div>
</div>

Note:

Section 1, context, about 2 minutes. One code base, two customers. Each customer sees only their own product: in the code, in the binary and in the documents.

---

<!-- .slide: data-auto-animate data-auto-animate-id="fm" -->

<p class="label">// customer input</p>

<div class="stage">
<div class="msg abs" style="left:0; top:10px;">
<div class="msg-head">From: Customer A<br>Subject: light for our party room</div>
<p>We need a <span class="w fragment mark c-common" data-fragment-index="0">light</span> for our party room. It shall <span class="w fragment mark c-disco" data-fragment-index="1" data-id="blink">blink</span> so people notice it. Please make it <span class="w fragment mark c-disco" data-fragment-index="1" data-id="green">green</span>. We want to <span class="w fragment mark c-common" data-fragment-index="0">switch it on and off</span> with one button.</p>
</div>
<div class="msg abs" style="left:460px; top:70px;">
<div class="msg-head">From: Customer B<br>Subject: bedroom lights</div>
<p>Our hotel needs a calm <span class="w fragment mark c-common" data-fragment-index="0">light</span> for the bedrooms. Guests shall <span class="w fragment mark c-sleep" data-fragment-index="1" data-id="dim">dim it by hand</span>. A soft <span class="w fragment mark c-sleep" data-fragment-index="1" data-id="purple">purple</span> works best. And of course a button to <span class="w fragment mark c-common" data-fragment-index="0">switch it on and off</span>.</p>
</div>
</div>

Note:

Section 2, the domain, about 5 minutes. Read both mails as they arrive. Step 1: what both want. Step 2: what only one of them wants. Next slide: the marked words leave the mails.

---

<!-- .slide: data-auto-animate data-auto-animate-id="fm" data-background-color="#0000a8" -->

<div class="stage">
<p class="label abs" style="left:0; top:-20px;">// features</p>
<p class="label abs fragment" style="left:560px; top:-20px;" data-fragment-index="0">// variants</p>
<div class="mc abs" style="left:0; top:30px; width:500px;"><div class="mc-box">
<div class="mc-title">SPLed light</div>
<ul class="mc-list">
<li>[ ] <span class="w" data-id="blink">Blinking</span></li>
<li>[ ] <span class="w" data-id="dim">Manual dimming</span></li>
<li>&nbsp;&nbsp;&nbsp; Color ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;( ) <span class="w" data-id="green">green</span></li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;( ) <span class="w" data-id="purple">purple</span></li>
</ul>
</div></div>
<div class="mc mini abs fragment bar-disco" style="left:560px; top:30px; width:300px;" data-fragment-index="0" data-id="card-disco"><div class="mc-box"><div class="mc-title">Disco</div><ul class="mc-list"><li>[*] Blinking</li><li>[ ] Manual dimming</li><li>(X) green</li></ul></div></div>
<div class="mc mini abs fragment bar-sleep" style="left:560px; top:250px; width:300px;" data-fragment-index="1" data-id="card-sleep"><div class="mc-box"><div class="mc-title">Sleep</div><ul class="mc-list"><li>[ ] Blinking</li><li>[*] Manual dimming</li><li>(X) purple</li></ul></div></div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The words only one customer wrote are now the menu. What both want is not modelled: there is nothing to toggle. The round brackets mean pick one. Then the two selections: two variants, each a name and a feature selection. Components join the variant later.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="fm" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li class="fragment cursor">[*] Feature model</li>
<li class="fragment cursor">[*] Variant model</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

First ticks: a feature model, with its rules, as the single source of what differs; and a variant model that names each product and its selection.

---

<p class="label">// the prototype</p>

<div class="stage">
<div class="layer abs app-layer" style="left:40px; top:20px;">Application: SPLed components</div>
<div class="zbox abs" style="left:40px; top:96px;">Zephyr RTOS<div class="zrow"><span class="zk">Subsystems</span><span class="chip">Shell</span><span class="chip">Logging</span></div><div class="zrow"><span class="zk">Device drivers</span><span class="chip">GPIO</span><span class="chip">LED strip (WS2812)</span></div><div class="zrow"><span class="zk">Kernel</span><span class="chip">Threads</span><span class="chip">Timers</span></div></div>
<div class="layer abs board" style="left:40px; top:290px;">ESP32-H2 dev board</div>
<div class="verdict abs" style="left:40px; top:370px;">The innovation team builds the first prototypes on Zephyr.</div>
</div>

Note:

Section 3, the prototype. The colleagues from the innovation department start. They pick Zephyr: boards, drivers, shell and logging come with it, and the dev board runs within days.

---

<!-- .slide: data-background-color="#0000a8" -->

<div class="mc">
<div class="mc-top">.config - Zephyr Kernel Configuration</div>
<div class="mc-box">
<div class="mc-title">Zephyr Kernel Configuration</div>
<div class="mc-help">Arrow keys navigate the menu. <b>&lt;Enter&gt;</b> selects submenus ---&gt;.</div>
<ul class="mc-list">
<li class="fragment cursor">&nbsp;&nbsp;&nbsp; Features ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Modules ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Board Options ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Hardware Configuration ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; General Kernel Options ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Device Drivers ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; C Library ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Subsystems and OS Services ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Build and Link Features ---&gt;</li>
<li>&nbsp;&nbsp;&nbsp; Boot Options ---&gt;</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Zephyr comes with Kconfig, a language for feature models, and kconfiglib, the Python tool that draws this menu (west build -t menuconfig). The application can add its own Kconfig. The innovation team is happy: two lines in app/Kconfig, and the SPLed features sit in the same menu as the Zephyr options. The menu is abridged; the entries are the real top-level menus of Zephyr.

---

<p class="label">// debugging without the board</p>

<div class="stage">
<div class="layer abs app-layer" style="left:40px; top:20px;">Application: SPLed components</div>
<div class="chip-test abs fragment" style="left:600px; top:28px;" data-fragment-index="1">+ ztest unit tests</div>
<div class="zbox abs" style="left:40px; top:96px;">Zephyr RTOS<div class="zrow"><span class="zk">Subsystems</span><span class="chip">Shell</span><span class="chip">Logging</span></div><div class="zrow"><span class="zk">Device drivers</span><span class="chip">GPIO</span><span class="chip">LED strip (WS2812)</span></div><div class="zrow"><span class="zk">Kernel</span><span class="chip">Threads</span><span class="chip">Timers</span></div></div>
<div class="layer abs board fragment fade-out" style="left:40px; top:290px;" data-fragment-index="0">ESP32-H2 dev board</div>
<div class="layer abs host fragment" style="left:40px; top:290px;" data-fragment-index="0">native_sim on the laptop</div>
<div class="verdict abs fragment" style="left:40px; top:370px;" data-fragment-index="1">Bugs are reproduced in unit tests on the host, not on the board.</div>
</div>

Note:

The first bugs come in. Debugging on the board is slow, so the team reproduces each problem in a unit test that runs on the laptop: Zephyr's native_sim board and ztest.

---

<!-- .slide: data-auto-animate data-auto-animate-id="fm2" -->

<p class="label">// variants × platforms</p>

<div class="stage">
<div class="card abs disco" style="left:0; top:120px;" data-id="card-disco"><b>Disco</b>Blinking, green</div>
<div class="card abs sleep" style="left:0; top:230px;" data-id="card-sleep"><b>Sleep</b>Manual dimming, purple</div>
<div class="col-head abs" style="left:280px; top:30px;">Dev board<small>Zephyr</small></div>
<div class="cell abs done" style="left:280px; top:110px;">prototype ✓</div>
<div class="cell abs done" style="left:280px; top:220px;">prototype ✓</div>
<div class="col-head abs fragment" style="left:590px; top:30px;" data-fragment-index="1">Series board<small>AUTOSAR, in-house hardware</small></div>
<div class="cell abs open fragment" style="left:590px; top:110px;" data-fragment-index="2">?</div>
<div class="cell abs open fragment" style="left:590px; top:220px;" data-fragment-index="2">?</div>
</div>

Note:

Each customer saw only their own demo. Then series development starts on another platform. Two empty cells.

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”<sup data-id="star">*</sup></div>
</div>

Note:

Section 4, about 2 minutes. Say it like the manager. Pause. Ask the room what they would do.

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:0; top:-20px; font-size:44px;" data-id="just">“Just port it.”<sup data-id="star">*</sup></div>
<div class="app abs" style="left:0; top:70px;" data-id="app"><b>Application</b><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="layer abs zephyr" style="left:0; top:200px; width:400px;" data-id="m-zephyr">Zephyr</div>
<div class="layer abs board" style="left:0; top:266px; width:400px;" data-id="m-dev">Dev board</div>
<div class="layer abs autosar" style="left:460px; top:200px; width:400px;" data-id="m-autosar">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:460px; top:266px; width:400px;" data-id="m-series">Series board, in-house</div>
</div>

Note:

This is how "just port it" looks from the manager's desk. The application is one block.

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:0; top:-20px; font-size:44px;" data-id="just">“Just port it.”<sup data-id="star">*</sup></div>
<div class="app abs" style="left:460px; top:70px;" data-id="app"><b>Application</b><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="layer abs zephyr ghost" style="left:0; top:200px; width:400px;" data-id="m-zephyr">Zephyr</div>
<div class="layer abs board ghost" style="left:0; top:266px; width:400px;" data-id="m-dev">Dev board</div>
<div class="layer abs autosar" style="left:460px; top:200px; width:400px;" data-id="m-autosar">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:460px; top:266px; width:400px;" data-id="m-series">Series board, in-house</div>
<div class="verdict abs" style="left:460px; top:340px;">Just move it over.</div>
</div>

Note:

Pick it up, put it down. Next slide: open the block and look inside.

---

<!-- .slide: data-auto-animate data-auto-animate-id="tangled" -->

<p class="label">// what is inside the block</p>

<div class="stage">
<div class="tile abs" style="left:40px; top:40px;" data-id="t1">light_controller</div>
<div class="tile abs" style="left:240px; top:40px;" data-id="t2">brightness_controller</div>
<div class="tile abs" style="left:440px; top:40px;" data-id="t3">power_signal_proc.</div>
<div class="tile abs" style="left:640px; top:40px;" data-id="t4">main_control_knob</div>
<div class="tile abs tied" style="left:40px; top:100px;" data-id="t5">power_button</div>
<div class="tile abs tied" style="left:240px; top:100px;" data-id="t6">led_interface</div>
<div class="tile abs tied" style="left:440px; top:100px;" data-id="t7">button_interface</div>
<div class="tile abs" style="left:640px; top:100px;" data-id="t8">rte</div>
<div class="layer abs zephyr" style="left:40px; top:180px;" data-id="zephyr">Zephyr</div>
<div class="layer abs board" style="left:40px; top:246px;" data-id="devboard">Dev board</div>
<div class="verdict abs" style="left:40px; top:330px;">Red: components that call Zephyr directly.</div>
</div>

Note:

Section 5, why it is not just, about 6 minutes. The components of SPLed. The red ones include Zephyr headers, call the kernel and use devicetree macros. It was the fastest way to get the demo running.

---

<!-- .slide: data-auto-animate data-auto-animate-id="tangled" -->

<p class="label">// just port it</p>

<div class="stage">
<div class="tile abs" style="left:40px; top:40px;" data-id="t1">light_controller</div>
<div class="tile abs" style="left:240px; top:40px;" data-id="t2">brightness_controller</div>
<div class="tile abs" style="left:440px; top:40px;" data-id="t3">power_signal_proc.</div>
<div class="tile abs" style="left:640px; top:40px;" data-id="t4">main_control_knob</div>
<div class="tile abs hole" style="left:40px; top:100px;"></div>
<div class="tile abs hole" style="left:240px; top:100px;"></div>
<div class="tile abs hole" style="left:440px; top:100px;"></div>
<div class="tile abs" style="left:640px; top:100px;" data-id="t8">rte</div>
<div class="layer abs autosar" style="left:40px; top:180px;">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:40px; top:246px;">Series board, in-house</div>
<div class="verdict abs" style="left:40px; top:310px;">Port = rewrite every red tile.</div>
<div class="tile abs tied ghost" style="left:60px; top:370px;" data-id="t5">power_button</div>
<div class="tile abs tied ghost" style="left:260px; top:370px;" data-id="t6">led_interface</div>
<div class="tile abs tied ghost" style="left:460px; top:370px;" data-id="t7">button_interface</div>
<div class="layer abs zephyr ghost" style="left:40px; top:416px;" data-id="zephyr">Zephyr</div>
</div>

Note:

The platform leaves, and the red tiles leave with it. The holes are the work.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bill" -->

<div class="stage">
<div class="just abs" style="left:0; top:0; font-size:44px;" data-id="just">“Just port it.”<sup data-id="star">*</sup></div>
<ol class="bill abs" style="left:40px; top:100px;">
<li class="fragment"><em>*</em> Replace every Zephyr call in the application</li>
<li class="fragment"><em>*</em> Describe every component again for AUTOSAR</li>
<li class="fragment"><em>*</em> Dig the two variants out of <code>prj.conf</code> files</li>
<li class="fragment"><em>*</em> Move the component list out of CMake</li>
<li class="fragment"><em>*</em> Rewrite the tests that ran under twister</li>
<li class="fragment"><em>*</em> Rebuild CI and relearn every tool</li>
</ol>
</div>

Note:

The asterisk is the small print of "just". One line per click. At the prj.conf line, say why: product options and board options sit in the same file, so someone has to sort them by hand.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios3" -->

<p class="label">// a day on the prototype team</p>

<div class="term">
<div class="head">~/.zsh_history</div>
<div><span class="n">101</span><span class="fragment cross" data-fragment-index="1">west build -b esp32h2_devkitm app -- -DFILE_SUFFIX=disco</span></div>
<div class="instead fragment" data-fragment-index="1">→ open the vendor configurator, export ARXML, run the RTE generator</div>
<div><span class="n">102</span><span class="fragment cross" data-fragment-index="2">west build -t menuconfig</span></div>
<div class="instead fragment" data-fragment-index="2">→ a different tool, a different file format</div>
<div><span class="n">103</span><span class="fragment cross" data-fragment-index="3">west twister -p native_sim -T app</span></div>
<div class="instead fragment" data-fragment-index="3">→ no simulator target, tests need a new home</div>
<div><span class="n">104</span><span class="fragment cross" data-fragment-index="4">west flash</span></div>
<div class="instead fragment" data-fragment-index="4">→ the vendor's flash script and debugger</div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

Not the code this time: the commands. Each one belongs to the platform. The way of working moves out with Zephyr.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="bios3" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] Feature model</li>
<li>[*] Variant model</li>
<li class="fragment cursor">[*] One product, several platforms</li>
<li class="fragment cursor">[*] A new platform leaves the products unchanged</li>
<li class="fragment cursor">[*] Product and platform choices in separate files</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

What the manager asked for, written as requirements.

---

<!-- .slide: data-auto-animate data-auto-animate-id="shell" -->

<p class="label">// with a thin shell</p>

<div class="stage">
<div class="tile abs" style="left:40px; top:40px;">light_controller</div>
<div class="tile abs" style="left:240px; top:40px;">brightness_controller</div>
<div class="tile abs" style="left:440px; top:40px;">power_signal_proc.</div>
<div class="tile abs" style="left:640px; top:40px;">main_control_knob</div>
<div class="tile abs" style="left:40px; top:100px;">power_button</div>
<div class="tile abs" style="left:240px; top:100px;">led_interface</div>
<div class="tile abs" style="left:440px; top:100px;">button_interface</div>
<div class="tile abs" style="left:640px; top:100px;">rte</div>
<div class="layer abs shell" style="left:40px; top:162px;" data-id="shell">zephyr shell: adapters for led, button, timer</div>
<div class="layer abs zephyr" style="left:40px; top:196px;" data-id="zephyr">Zephyr</div>
<div class="layer abs board" style="left:40px; top:262px;" data-id="devboard">Dev board</div>
<div class="verdict abs" style="left:40px; top:340px;">No component includes a platform header.</div>
</div>

Note:

Section 6, can we improve, about 5 minutes. Same components. The only code that knows Zephyr is the shell.

---

<!-- .slide: data-auto-animate data-auto-animate-id="shell" -->

<p class="label">// just port it, again</p>

<div class="stage">
<div class="tile abs" style="left:40px; top:40px;">light_controller</div>
<div class="tile abs" style="left:240px; top:40px;">brightness_controller</div>
<div class="tile abs" style="left:440px; top:40px;">power_signal_proc.</div>
<div class="tile abs" style="left:640px; top:40px;">main_control_knob</div>
<div class="tile abs" style="left:40px; top:100px;">power_button</div>
<div class="tile abs" style="left:240px; top:100px;">led_interface</div>
<div class="tile abs" style="left:440px; top:100px;">button_interface</div>
<div class="tile abs" style="left:640px; top:100px;">rte</div>
<div class="layer abs shell" style="left:40px; top:162px;">autosar shell: one SWC, RTE ports as adapters</div>
<div class="layer abs autosar" style="left:40px; top:196px;">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:40px; top:262px;">Series board, in-house</div>
<div class="verdict abs" style="left:40px; top:330px;">Port = write a new shell.</div>
<div class="layer abs shell ghost" style="left:40px; top:390px;" data-id="shell">zephyr shell: adapters for led, button, timer</div>
<div class="layer abs zephyr ghost" style="left:40px; top:420px;" data-id="zephyr">Zephyr</div>
</div>

Note:

The platform leaves with its shell. Every tile stays. This is the answer the manager wanted.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios1" -->

<p class="label">// the same light, four altitudes</p>

<div class="stage">
<div class="step l1 abs" style="left:0; top:0;"><small>customer · sales</small>“A green light that blinks.”</div>
<div class="step l2 abs fragment" style="left:120px; top:110px;"><small>product features · system engineer</small>BLINKING=y &nbsp; COLOR_GREEN=y</div>
<div class="step l3 abs fragment" style="left:240px; top:210px;"><small>platform features · software engineer</small>WS2812_STRIP_SPI=y</div>
<div class="step l4 abs fragment" style="left:360px; top:300px;"><small>platform value · hardware engineer</small>DELAY_T1H = 700 ns × CPU clock / 10⁹<br>(number of NOPs for a high bit)</div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The platform changes, the customer's sentence does not. Each click goes one level down. The room recognises their own level. The DELAY_T1H default is the real formula from Zephyr's Kconfig.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="bios1" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] Feature model</li>
<li>[*] Variant model</li>
<li>[*] One product, several platforms</li>
<li>[*] A new platform leaves the products unchanged</li>
<li>[*] Product and platform choices in separate files</li>
<li class="fragment cursor">[*] Platform model</li>
<li class="fragment cursor">[*] Two feature models</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

The platform is a model of its own: middle layer, hardware and its own components, such as the shell. And its features live in a feature model of their own.

---

<!-- .slide: data-auto-animate data-auto-animate-id="comp" -->

<p class="label">// a component</p>

<div class="stage">
<div class="tile abs" style="left:350px; top:180px;" data-id="comp">light_controller</div>
</div>

Note:

One tile from the stack. Next click: open it.

---

<!-- .slide: data-auto-animate data-auto-animate-id="comp" -->

<p class="label">// a component</p>

<div class="stage">
<div class="comp abs" style="left:130px; top:40px;" data-id="comp">
<b>light_controller</b> &nbsp; <span class="tag">scope: SPL</span><br>
<span class="k">code</span> src/light_controller.c, .h<br>
<span class="k">tests</span> test/test_light_controller.cc<br>
<span class="k">docs</span> doc/index.md<br>
<span class="k">features</span> KConfig
</div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

A component is not a source file. It carries its code, its tests, its docs and its own options, and it says where it belongs: the whole SPL, one variant, one platform, or one pair.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="comp" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] Feature model</li>
<li>[*] Variant model</li>
<li>[*] One product, several platforms</li>
<li>[*] A new platform leaves the products unchanged</li>
<li>[*] Product and platform choices in separate files</li>
<li>[*] Platform model</li>
<li>[*] Two feature models</li>
<li class="fragment cursor">[*] Component model</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Components with their production, test and documentation files.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios7" -->

<p class="label">// who can read your model?</p>

<div class="stage">
<svg class="readers-lines abs" width="880" height="470" style="left:0; top:0;">
<line x1="420" y1="120" x2="600" y2="40"/>
<line x1="420" y1="140" x2="600" y2="110"/>
<line x1="420" y1="160" x2="600" y2="180"/>
<line x1="420" y1="180" x2="600" y2="250"/>
<line x1="420" y1="400" x2="600" y2="400"/>
</svg>
<div class="code abs" style="left:0; top:0;"><span class="f">variants/Disco/yanga.yaml</span>
- name: Disco
  components:
  - rte
  - spled
  - light_application
  feature_selection:
    file: variants/Disco/config.txt</div>
<div class="code abs" style="left:0; top:300px;"><span class="f">app/CMakeLists.txt</span>
target_sources_ifdef(CONFIG_SHELL
    app PRIVATE src/buttons_shell.c)</div>
<div class="reader abs" style="left:610px; top:22px;">the build</div>
<div class="reader abs" style="left:610px; top:92px;">the variant report</div>
<div class="reader abs" style="left:610px; top:162px;">the docs build</div>
<div class="reader abs" style="left:610px; top:232px;">the CI matrix</div>
<div class="reader abs" style="left:610px; top:382px;">the build</div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

Data has many readers. Code has one: the tool that runs it. Same idea as a GitHub workflow file: GitHub draws the job graph from it without running it.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="bios7" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] Feature model</li>
<li>[*] Variant model</li>
<li>[*] One product, several platforms</li>
<li>[*] A new platform leaves the products unchanged</li>
<li>[*] Product and platform choices in separate files</li>
<li>[*] Platform model</li>
<li>[*] Two feature models</li>
<li>[*] Component model</li>
<li class="fragment cursor">[*] Documentation and reports</li>
<li class="fragment cursor">[*] Models as data</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Models as data, and the readers that need them: reports and documentation.

---

<p class="label">// where does Disco live?</p>

<div class="where">
<div>
<h4>Zephyr</h4>
<div class="code"><span class="f">app/prj_disco.conf</span>
CONFIG_GPIO=y
CONFIG_SHELL=y
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y</div>
<div class="code"><span class="f">app/CMakeLists.txt</span>
target_sources_ifdef(
  CONFIG_SHELL ...)</div>
</div>
<div class="fragment">
<h4>spl-core</h4>
<div class="code"><span class="f">variants/Disco/config.txt</span>
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y</div>
<div class="code"><span class="f">variants/Disco/parts.cmake</span>
spl_add_component(
  components/light_controller)</div>
</div>
<div class="fragment">
<h4>yanga</h4>
<div class="code"><span class="f">variants/Disco/config.txt</span>
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y</div>
<div class="code"><span class="f">variants/Disco/yanga.yaml</span>
- name: Disco
  components: [rte, spled, ...]</div>
</div>
</div>

Note:

Section 7, the three frameworks, about 6 minutes. The same variant in three tools, as the files show it. No scores: the audience sees where product and board options meet, and where the component list lives.

---

<p class="label">// TODO</p>

More side-by-side slides: where the platform lives, where the components live, where the selections live. One question per slide, the real files of each tool as the answer.

Note:

Open: which questions get a slide. Candidates follow the requirements R1 to R10.

---

<!-- .slide: data-auto-animate data-auto-animate-id="close" -->

<div class="stage">
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”</div>
<div class="verdict abs fragment" style="left:110px; top:300px; font-size:40px;">“Sure. New shell, same application.”</div>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

Section 8, about 2 minutes. The opening line comes back, without the asterisk.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="close" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Take a photo</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] R1 One product, several platforms</li>
<li>[*] R2 A new platform leaves the products unchanged</li>
<li>[*] R3 Documentation and reports</li>
<li>[*] R4 Feature model</li>
<li>[*] R5 Variant model</li>
<li>[*] R6 Platform model</li>
<li>[*] R7 Component model</li>
<li>[*] R8 Two feature models</li>
<li>[*] R9 Product and platform choices in separate files</li>
<li>[*] R10 Models as data</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

The photo slide. Leave it up while people take pictures, then go to questions.

---

### Questions?

<div class="qr">

![QR code of the slides](../images/qr_zephyr_meets_sple.png)

</div>

https://avengineers.github.io/ESE-2026/docs/zephyr_meets_sple/ <!-- .element: class="deck-url" -->

---

### Some Links

- [We@GitHub](https://github.com/avengineers)
- [Printable Slides](https://avengineers.github.io/ESE-2026/docs/zephyr_meets_sple/?print-pdf)
