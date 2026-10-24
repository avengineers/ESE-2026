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
<div class="ie-photo"><img src="../images/alexandru.png" alt="Alexandru"></div>
<div class="ie-name">Alexandru Maxiniuc</div>
<p>I am interested in engineering software product lines, software architecture and build systems.</p>
<div class="ie-new"><span class="ie-blink">NEW!</span> Updated for the ESE Kongress 2026</div>
<div class="ie-uc">UNDER CONSTRUCTION</div>
<p class="ie-links"><a>[ About me ]</a> <a>[ My projects ]</a> <a>[ Guestbook ]</a> <a>[ Links ]</a> <a>[ Webring ]</a></p>
<div class="ie-counter">You are visitor number <span>000042</span></div>
<p class="ie-best">Best viewed with Internet Explorer 5.0 at 800x600</p>
</div>
<div class="ie-status"><span><span class="ie-done">Done</span><span class="ie-loading">(1 item remaining) Downloading picture http://www.maxiniuc.com/me.jpg...</span></span><span>🌐 Internet</span></div>
</div>

Note:

The old homepage, "updated for the conference". The sentence on the page is from the About page of maxiniuc.com.

I started with embedded software engineering when websites looked like this and Windows 98 was the hyped OS.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="now">Two customers, one product line</li>
<li>From wishes to features</li>
<li>A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
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

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="now">From wishes to features</li>
<li>A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>Two customers write what they want.</p>
</div>
</div>

Note:

Chapter 2: From wishes to features. Say the sentence and go on.

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

<!-- .slide: data-auto-animate data-auto-animate-id="concerns" -->

<p class="label">// separation of concerns</p>

<div class="stage">
<div class="fragment" data-fragment-index="0">
<span class="wish c-common abs" style="left:0; top:38px;">light</span>
<span class="wish c-common abs" style="left:0; top:108px;">switch it on and off</span>
<span class="wish c-sleep abs" style="left:0; top:178px;">dim it by hand</span>
<span class="wish c-disco abs" style="left:0; top:248px;">blink</span>
<span class="wish c-disco abs" style="left:80px; top:248px;">green</span>
<span class="wish c-sleep abs" style="left:170px; top:248px;">purple</span>
</div>
<div class="fragment" data-fragment-index="1">
<span class="arrow abs" style="left:400px; top:30px;">→</span>
<div class="tile abs" style="left:480px; top:30px;">light_controller</div>
<span class="arrow abs" style="left:400px; top:100px;">→</span>
<div class="tile abs" style="left:480px; top:100px;">power_button</div>
<div class="tile abs" style="left:680px; top:100px;">power_signal_proc</div>
<span class="arrow abs" style="left:400px; top:170px;">→</span>
<div class="tile abs" style="left:480px; top:170px;">brightness_controller</div>
<span class="arrow abs" style="left:400px; top:240px;">→</span>
<div class="tile option abs" style="left:480px; top:240px; width:380px;">options inside light_controller</div>
</div>
<p class="label abs fragment" style="left:480px; top:-30px;" data-fragment-index="1">// components</p>
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

Before anyone writes code: which part does what. With separation of concerns, you think in parts of the code that each do one thing. Later, these parts become your components. The light, the button and its signal, the dimming: each concern gets a component. Blinking and the color are options of light_controller, not components. Features and components are not one to one. These are the components in src/ of the first application, and the tiles come back in chapter 5.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="concerns" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box" data-id="bios">
<div class="mc-title">Requirements</div>
<div class="mc-help">Collected along the story. <b>&lt;Y&gt;</b> includes, <b>&lt;N&gt;</b> excludes, <b>&lt;?&gt;</b> asks the speaker.</div>
<ul class="mc-list">
<li>[*] Feature model</li>
<li>[*] Variant model</li>
<li class="fragment cursor">[*] Component model</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Third tick: a component model. Each concern lives in its own component, and a feature is either a component or an option inside one.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="now">A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>We know the features, the variants and the components. Now they have to run on a board.</p>
</div>
</div>

Note:

Chapter 3: A prototype on Zephyr. Say the sentence and go on.

---

<p class="label">// the decision</p>

<div class="stage">
<div class="msg abs" style="left:78px; top:40px; width:680px;">
<div class="msg-head">From: Innovation team<br>Subject: prototypes for Disco and Sleep</div>
<p>We build the prototypes on the <span class="w fragment mark c-common">ESP32-H2 dev board</span> with <span class="w fragment mark c-common">Zephyr</span>. Drivers, shell and logging come with it, so the board runs <span class="w fragment mark c-common">within days</span>.</p>
</div>
</div>

Note:

Section 3, the prototype. The innovation department decides: a dev board and Zephyr. Boards, drivers, shell and logging come with Zephyr, and the dev board runs within days. Stress "within days": Zephyr supports this board, so it runs almost at once.

---

<p class="label">// what Zephyr brings</p>

<div class="stage">
<div class="zbox abs" style="left:0; top:20px; width:380px;">Software components<div><span class="chip">Kernel</span><span class="chip">Device drivers</span><span class="chip">Shell</span><span class="chip">Logging</span><span class="chip">HAL modules</span></div></div>
<div class="zbox abs fragment" style="left:446px; top:20px; width:380px;">Tooling and build environment<div><span class="chip">west</span><span class="chip">CMake</span><span class="chip">Kconfig</span><span class="chip">devicetree</span><span class="chip">Zephyr SDK</span><span class="chip">Twister</span></div></div>
<div class="verdict abs fragment" style="left:0; top:180px;">The team takes both: the code and the way of working.</div>
</div>

Note:

A Zephyr project has two parts. The software components: kernel, drivers, subsystems such as shell and logging, and the vendor HAL as a module. And the tooling: west fetches the repositories and runs the build, CMake builds, Kconfig and devicetree configure, the SDK compiles, Twister runs the tests. Remember the right box: in chapter 5 it leaves with Zephyr.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zapp" -->

<p class="label">// the first application</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:700px; font-size:22px;" data-id="tree">app/
├── CMakeLists.txt   <span class="f"># finds Zephyr, lists the sources</span>
├── Kconfig          <span class="f"># the SPLed features</span>
├── prj.conf         <span class="f"># the selection for this build</span>
└── src/             <span class="f"># the SPLed components</span></div>
</div>

Note:

The innovation team creates the first Zephyr application. A folder with four entries, and west, CMake and Kconfig know what to do with each of them. Now we ask, model by model: where are the features, the variants and the components?

---

<!-- .slide: data-auto-animate data-auto-animate-id="zapp" -->

<p class="label">// where is the feature model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="tree">app/
├── CMakeLists.txt
├── <span class="hl">Kconfig</span>
├── prj.conf
└── src/</div>
<div class="code abs" style="left:320px; top:20px; width:400px; font-size:16px;"><span class="f blk">app/Kconfig</span><span class="fragment hl-current blk">menu "Features"
    config BLINKING
        bool "Blinking"
    config MANUAL_DIMMING
        bool "Manual dimming"
    choice
        prompt "Color"
        config COLOR_GREEN
            bool "green"
        config COLOR_PURPLE
            bool "purple"
    endchoice
endmenu</span><span class="fragment hl-current blk">source "Kconfig.zephyr"</span></div>
</div>

Note:

The feature model is app/Kconfig. First click: the menu, with our features from the customer e-mails and the choice of a color. Second click: the last line pulls in all the options of Zephyr, and Zephyr has a lot of them.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zvar" -->

<p class="label">// where is the variant model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="tree">app/
├── CMakeLists.txt
├── Kconfig
├── prj.conf
├── <span class="hl">prj<span class="w fragment mark c-disco" data-fragment-index="6">_disco</span>.conf</span>
├── <span class="hl">prj_sleep.conf</span>
└── src/</div>
<div class="code abs bar-disco fragment" data-fragment-index="0" style="left:320px; top:20px; width:240px; font-size:16px;"><span class="f">app/prj<span class="w fragment mark c-disco" data-fragment-index="6">_disco</span>.conf</span>
CONFIG_GPIO=y
CONFIG_SHELL=y
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y</div>
<div class="code abs bar-sleep fragment" data-fragment-index="1" style="left:600px; top:20px; width:240px; font-size:16px;"><span class="f">app/prj_sleep.conf</span>
CONFIG_GPIO=y
CONFIG_SHELL=y
CONFIG_MANUAL_DIMMING=y
CONFIG_COLOR_PURPLE=y</div>
<div class="term abs fragment" data-fragment-index="2" style="left:0; top:270px; width:836px;">
<div class="head">terminal</div>
<div>$ west build <span class="fragment" data-fragment-index="3">-b esp32h2_devkitm</span> <span class="fragment" data-fragment-index="4">app</span> <span class="fragment" data-fragment-index="5">-- -D<span class="w fragment mark c-disco" data-fragment-index="6">FILE_SUFFIX=disco</span></span></div>
</div>
</div>

Note:

Two variants, two files, written by hand. menuconfig shows the options, but saves to the build folder. To keep a selection, save a minimal configuration with D and copy it here. The file with the suffix replaces prj.conf, it does not add to it: GPIO and SHELL are in both files. The command: FILE_SUFFIX=disco takes prj_disco.conf; without such a file, Zephyr falls back to prj.conf.

---

<p class="label">// from the selection to the code</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:400px; font-size:14px;"><span class="f">build/zephyr/include/generated/zephyr/autoconf.h</span>
#define CONFIG_GPIO 1
#define CONFIG_SHELL 1
#define CONFIG_BLINKING 1
#define CONFIG_COLOR_GREEN 1
<span class="f">...</span></div>
<span class="arrow abs fragment" style="left:200px; top:180px;" data-fragment-index="0">↓</span>
<div class="code abs fragment" style="left:0; top:240px; width:400px; font-size:14px;" data-fragment-index="0"><span class="f">app/src/light_controller.c</span>
#ifdef CONFIG_BLINKING
    ...
#endif</div>
<div class="code abs fragment" style="left:448px; top:20px; width:400px; font-size:14px;" data-fragment-index="1"><span class="f">build/zephyr/.config</span>
CONFIG_GPIO=y
CONFIG_SHELL=y
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y
<span class="f">...</span></div>
<span class="arrow abs fragment" style="left:648px; top:180px;" data-fragment-index="2">↓</span>
<div class="code abs fragment" style="left:448px; top:240px; width:400px; font-size:14px;" data-fragment-index="2"><span class="f">app/CMakeLists.txt</span>
target_sources_ifdef(CONFIG_BLINKING ...)</div>
</div>

Note:

The build turns the selection of the variant into two files. autoconf.h has one #define per option, and Zephyr passes it to every C file with -imacros: the components read CONFIG_BLINKING without an include. zephyr/.config has the same options for CMake: each one becomes a CMake variable, so the build system can add or leave out sources. Both files also hold every Zephyr option, not only ours.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zvar" -->

<p class="label">// where is the component model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="tree">app/
├── <span class="hl">CMakeLists.txt</span>
├── Kconfig
├── prj.conf
├── prj_disco.conf
├── prj_sleep.conf
└── src/</div>
<div class="code abs" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f">app/CMakeLists.txt</span>
<span class="f">cmake_minimum_required(VERSION 3.20.0)</span>
<span class="f">find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})</span>
<span class="f">project(spled)</span>
target_sources(app PRIVATE
    src/light_controller.c
    src/power_button.c
    src/power_signal_processing.c)
target_sources_ifdef(CONFIG_MANUAL_DIMMING
    app PRIVATE src/brightness_controller.c)</div>
</div>

Note:

The component model is CMakeLists.txt. A component is a list of source files, and a Kconfig option decides whether they are built: brightness_controller only for Sleep. That is all Zephyr knows about a component.

---

<!-- .slide: data-background-color="#0000a8" -->

<div class="mc">
<div class="mc-top">.config - Zephyr as a development environment for a product line</div>
<div class="mc-box">
<div class="mc-title">Requirements</div>
<div class="mc-help">What Zephyr gives the prototype.</div>
<ul class="mc-list">
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="1">*</span>] Feature model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="1">Kconfig: options, rules and a menu</span></li>
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="2">*</span>] Variant model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="2">one .conf file per variant, picked by FILE_SUFFIX</span></li>
<li class="fragment" data-fragment-index="0">[ ] Component model<span class="why fragment" data-fragment-index="3">just a list of sources in CMake</span></li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

All three come in unticked. Then tick the feature model and the variant model. The component model stays unticked. Zephyr gives us a feature model: Kconfig. A variant model only partly: the name is a file suffix, the selection is a file. Nothing lists the variants or describes them. A component model only partly: a component is a list of sources, without its tests and docs.

---

<p class="label">// debugging without the board</p>

<div class="stage">
<div class="layer abs app-layer" style="left:40px; top:20px;">Application: SPLed components</div>
<div class="chip-test abs fragment" style="left:600px; top:28px;" data-fragment-index="1">+ ztest unit tests</div>
<div class="zbox abs" style="left:40px; top:96px;">Zephyr RTOS<div class="zrow"><span class="zk">Subsystems</span><span class="chip">Shell</span><span class="chip">Logging</span></div><div class="zrow"><span class="zk">Device drivers</span><span class="chip">GPIO</span><span class="chip">LED strip (WS2812)</span></div><div class="zrow"><span class="zk">Kernel</span><span class="chip">Threads</span><span class="chip">Timers</span></div></div>
<div class="layer abs board fragment fade-out" style="left:40px; top:290px;" data-fragment-index="0">ESP32-H2 dev board</div>
<div class="layer abs host fragment" style="left:40px; top:290px;" data-fragment-index="0">native_sim on the host PC</div>
<div class="verdict abs fragment" style="left:40px; top:370px;" data-fragment-index="1">Bugs are reproduced in unit tests on the host, not on the board.</div>
</div>

Note:

The first bugs come in. Debugging on the board is slow, so the team reproduces each problem in a unit test that runs on the host PC: Zephyr's native_sim board and ztest.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="now">The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>The business unit takes over: the same features and variants, a different platform.</p>
</div>
</div>

Note:

Chapter 4: The series product on AUTOSAR. Same questions as for the prototype.

---

<p class="label">// the decision</p>

<div class="stage">
<div class="msg abs" style="left:78px; top:40px; width:680px;">
<div class="msg-head">From: Business Unit Light<br>Subject: series development for Disco and Sleep</div>
<p>We build the series products on our <span class="w fragment mark c-common">in-house board</span> with <span class="w fragment mark c-common">AUTOSAR</span>. Our product lines are built with <span class="w fragment mark c-common">spl-core</span>, and the safety case needs a qualified stack.</p>
</div>
</div>

Note:

Section 4, the series product. The business unit decides: its own board with an off-the-shelf MCU, AUTOSAR Classic, and spl-core as the build environment it already uses for its product lines.

---

<p class="label">// what the series platform brings</p>

<div class="stage">
<div class="zbox abs" style="left:0; top:20px; width:380px;">Software components<div><span class="chip">OS</span><span class="chip">RTE</span><span class="chip">COM</span><span class="chip">I/O hardware abstraction</span><span class="chip">MCAL</span></div></div>
<div class="zbox abs fragment" style="left:446px; top:20px; width:380px;">Tooling and build environment<div><span class="chip">Vendor configurator</span><span class="chip">ARXML</span><span class="chip">RTE generator</span><span class="chip">spl-core</span><span class="chip">CMake</span><span class="chip">Kconfig</span><span class="chip">GoogleTest</span></div></div>
<div class="verdict abs fragment" style="left:0; top:200px;">Again both: the code and the way of working. None of it is Zephyr's.</div>
</div>

Note:

The same two boxes as for Zephyr. The software components of AUTOSAR Classic: OS, RTE, communication, the I/O hardware abstraction and the MCAL drivers. The tooling: the AUTOSAR vendor's configurator, ARXML and the RTE generator, plus spl-core, a set of CMake functions with Kconfig for the features and GoogleTest for the unit tests. The AUTOSAR boxes are generic; no open-source SPLed port runs on AUTOSAR.

---

<!-- .slide: data-auto-animate data-auto-animate-id="sapp" -->

<p class="label">// the first series application</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:700px; font-size:22px;" data-id="stree">SPLed/
├── CMakeLists.txt   <span class="f"># includes spl-core</span>
├── KConfig          <span class="f"># the SPLed features</span>
├── variants/        <span class="f"># one folder per variant</span>
└── components/      <span class="f"># one folder per component</span></div>
</div>

Note:

The business unit sets up the series project the spl-core way. A folder with four entries. The same three questions: where are the features, the variants and the components?

---

<!-- .slide: data-auto-animate data-auto-animate-id="sapp" -->

<p class="label">// where is the feature model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="stree">SPLed/
├── CMakeLists.txt
├── <span class="hl">KConfig</span>
├── variants/
└── components/</div>
<div class="code abs" style="left:320px; top:20px; width:440px; font-size:16px;"><span class="f blk">KConfig</span><span class="blk">mainmenu "SPLed"</span><span class="fragment hl-current blk">source "$(SPL_CORE_DIR)/config/KConfig"</span><span class="fragment hl-current blk">menu "Features"
    config BLINKING
        bool "Blinking"
    config MANUAL_DIMMING
        bool "Manual dimming"
    choice
        prompt "Color"
        config COLOR_GREEN
            bool "green"
        config COLOR_PURPLE
            bool "purple"
    endchoice
endmenu</span></div>
</div>

Note:

The feature model is KConfig again, the same language as in the prototype. First click: spl-core adds a few options of its own, not the thousands of Zephyr. Second click: the same features. The real file names the dimming option BRIGHTNESS_ADJUSTMENT_MANUAL; as in chapter 3, the slide uses short names.

---

<!-- .slide: data-auto-animate data-auto-animate-id="svar" -->

<p class="label">// where is the variant model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:270px; font-size:16px;" data-id="stree">SPLed/
├── KConfig
├── variants/
│   ├── Disco/
│   │   ├── <span class="hl">config.txt</span>
│   │   └── <span class="hl">parts.cmake</span>
│   └── Sleep/
└── components/</div>
<div class="code abs bar-disco fragment" data-fragment-index="0" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f">variants/Disco/config.txt</span>
CONFIG_BLINKING=y
CONFIG_COLOR_GREEN=y</div>
<div class="code abs bar-disco fragment" data-fragment-index="1" style="left:320px; top:130px; width:520px; font-size:16px;"><span class="f">variants/Disco/parts.cmake</span>
spl_add_component(components/light_controller)
spl_add_component(components/power_button)
spl_add_component(components/power_signal_processing)
<span class="f">...</span></div>
<div class="term abs fragment" data-fragment-index="2" style="left:0; top:300px; width:836px;">
<div class="head">terminal</div>
<div>$ ./build.sh --build --variant Disco</div>
</div>
</div>

Note:

A variant is a folder with its name. config.txt holds the feature selection, parts.cmake lists the components of this variant. No board options in the selection, unlike prj_disco.conf. A third file, config.cmake, picks the toolchain. The real config.txt also holds a few build settings such as the name of the output file.

---

<!-- .slide: data-auto-animate data-auto-animate-id="svar" -->

<p class="label">// where is the component model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:270px; font-size:16px;" data-id="stree">components/
└── light_controller/
    ├── <span class="hl">CMakeLists.txt</span>
    ├── KConfig
    ├── src/
    ├── test/
    └── doc/</div>
<div class="code abs" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f">components/light_controller/CMakeLists.txt</span>
spl_add_source(src/light_controller.c)
spl_add_test_source(test/test_light_controller.cc)
spl_add_required_interface(components/rte)
spl_create_component(LONG_NAME "Light Controller")</div>
</div>

Note:

A component is a folder with its sources, its unit tests, its documentation and its own options, and a CMakeLists.txt that declares them with spl-core functions. Compare chapter 3: there a component was a line in a list of sources.

---

<!-- .slide: data-background-color="#0000a8" -->

<div class="mc">
<div class="mc-top">.config - spl-core as a development environment for a product line</div>
<div class="mc-box">
<div class="mc-title">Requirements</div>
<div class="mc-help">What spl-core gives the series project.</div>
<ul class="mc-list">
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="1">*</span>] Feature model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="1">Kconfig, as in Zephyr</span></li>
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="2">*</span>] Variant model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="2">a folder per variant: selection and component list</span></li>
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="3">*</span>] Component model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="3">sources, tests and docs per component, in CMake</span></li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

All three come in unticked, then all three get ticked. spl-core has a variant model and a component model. Remember where they live: in CMake files that only the build reads. That comes back in chapter 6.

---

<p class="label">// debugging without the board</p>

<div class="stage">
<div class="layer abs app-layer" style="left:40px; top:20px;">Application: SPLed components</div>
<div class="zbox abs fragment fade-out" style="left:40px; top:96px;" data-fragment-index="0">AUTOSAR Classic<div class="zrow"><span class="zk">Services</span><span class="chip">OS</span><span class="chip">COM</span></div><div class="zrow"><span class="zk">Runtime</span><span class="chip">RTE</span></div><div class="zrow"><span class="zk">Drivers</span><span class="chip">I/O hardware abstraction</span><span class="chip">MCAL</span></div></div>
<div class="layer abs board series fragment fade-out" style="left:40px; top:290px;" data-fragment-index="0">In-house board</div>
<div class="layer abs mocks fragment" style="left:40px; top:96px;" data-fragment-index="0">Mocks, generated from the headers</div>
<div class="layer abs host fragment" style="left:40px; top:290px;" data-fragment-index="0">GoogleTest on the host PC</div>
<div class="verdict abs fragment" style="left:40px; top:370px;" data-fragment-index="1">Each component is tested alone, against generated mocks.</div>
</div>

Note:

spl-core's test build kit compiles each component with its unit tests for the host PC: no AUTOSAR, no board. The mocks for everything a component calls are generated (hammocking). Compare chapter 3: native_sim runs the whole Zephyr on the host, here each component runs alone. Command: ./build.sh --build --build-kit test --variant Disco.

---

<!-- .slide: data-auto-animate data-auto-animate-id="fm2" -->

<p class="label">// variants × platforms</p>

<div class="stage">
<div class="card abs disco" style="left:0; top:120px;" data-id="card-disco"><b>Disco</b>Blinking, green</div>
<div class="card abs sleep" style="left:0; top:230px;" data-id="card-sleep"><b>Sleep</b>Manual dimming, purple</div>
<div class="col-head abs" style="left:280px; top:30px;">Dev board<small>Zephyr</small></div>
<div class="cell abs done" style="left:280px; top:110px;">prototype ✓</div>
<div class="cell abs done" style="left:280px; top:220px;">prototype ✓</div>
<div class="col-head abs fragment" style="left:590px; top:30px;" data-fragment-index="1">In-house board<small>AUTOSAR + spl-core</small></div>
<div class="cell abs open fragment" style="left:590px; top:110px;" data-fragment-index="2">?</div>
<div class="cell abs open fragment" style="left:590px; top:220px;" data-fragment-index="2">?</div>
</div>

Note:

Each customer saw only their own demo. The series project is set up, with its own three models, but without the application. Two empty cells.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="now">Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>The series product runs on another platform. How hard can the move be?</p>
</div>
</div>

Note:

Chapter 5: Just port it? Say the sentence and go on.

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
<li class="fragment"><em>*</em> Wrap the application for the RTE and describe it in ARXML</li>
<li class="fragment"><em>*</em> Move the variants from <code>prj_*.conf</code> to <code>variants/</code></li>
<li class="fragment"><em>*</em> Turn each list of sources into an spl-core component</li>
<li class="fragment"><em>*</em> Rewrite the ztest tests in GoogleTest</li>
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
<div class="instead fragment" data-fragment-index="1">→ ./build.sh --build --variant Disco, after the vendor configurator and the RTE generator</div>
<div><span class="n">102</span><span class="fragment cross" data-fragment-index="2">west build -t menuconfig</span></div>
<div class="instead fragment" data-fragment-index="2">→ the same Kconfig, but variants/Disco/config.txt instead of prj_disco.conf</div>
<div><span class="n">103</span><span class="fragment cross" data-fragment-index="3">west twister -p native_sim -T app</span></div>
<div class="instead fragment" data-fragment-index="3">→ ./build.sh --build --build-kit test: GoogleTest, not ztest</div>
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
<li>[*] Component model</li>
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

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="done">Just port it?</li>
<li class="now">What if: one product line, three platforms</li>
<li>Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>What if the prototype and the series product came from one product line?</p>
</div>
</div>

Note:

Chapter 6: What if. Say the sentence and go on.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

<p class="label">// one product line, three platforms</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:760px; font-size:22px;" data-id="ytree">SPLed/
├── yanga.yaml       <span class="f"># the pipeline and the feature model</span>
├── KConfig          <span class="f"># the product features</span>
├── variants/        <span class="f"># Disco, Sleep</span>
├── components/      <span class="f"># the SPLed components</span>
└── platforms/       <span class="f"># zephyr, autosar, gtest</span></div>
</div>

Note:

The what-if, built with yanga. One repository, one application, and three platforms: Zephyr for the prototype on the dev board, AUTOSAR for the series board, and gtest for the unit tests on the host. The zephyr and gtest platforms exist in the open SPLed repository; the autosar platform is the what-if.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

<p class="label">// where is the variant model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="ytree">SPLed/
├── yanga.yaml
├── KConfig
├── variants/
│   └── Disco/
│       ├── <span class="hl">yanga.yaml</span>
│       └── config.txt
├── components/
└── platforms/</div>
<div class="code abs bar-disco" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f">variants/Disco/yanga.yaml</span>
variants:
- name: Disco
  description: The LED blinks and one can change ...
  components: [rte, spled, light_application]
  feature_selection:
    file: variants/Disco/config.txt
  <span class="fragment hl-current">platforms:
    zephyr_esp32h2: ...
    autosar: ...
    gtest: ...</span></div>
</div>

Note:

The variant is data: its name, a description, its components and its feature selection. The click: what this variant needs on each platform, for example a selection of Zephyr options. In the real file the platforms are zephyr_esp32h2, tc375, arduino and gtest; autosar is the what-if.

---

<p class="label">// where is the platform model?</p>

<div class="stage">
<div class="zbox abs" style="left:0; top:20px; width:250px;">zephyr_esp32h2<div class="zrow"><span class="chip">west + board</span></div><div class="zrow"><span class="chip">Zephyr adapters</span></div></div>
<div class="zbox abs fragment" style="left:296px; top:20px; width:250px;">autosar<div class="zrow"><span class="chip">vendor tools</span></div><div class="zrow"><span class="chip">RTE adapters</span></div></div>
<div class="zbox abs fragment" style="left:592px; top:20px; width:250px;">gtest<div class="zrow"><span class="chip">GoogleTest</span></div><div class="zrow"><span class="chip">generated mocks</span></div></div>
<div class="verdict abs fragment" style="left:0; top:200px;">A platform brings its own tools and its own components.</div>
</div>

Note:

A platform is a model of its own: how to build, which tools, and which components only this platform has, such as the adapters to the drivers. zephyr_esp32h2 and gtest are real platforms of SPLed; autosar is the what-if. The application components are the same on all three.

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
<li>[*] Component model</li>
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
<li>[*] Component model</li>
<li>[*] One product, several platforms</li>
<li>[*] A new platform leaves the products unchanged</li>
<li>[*] Product and platform choices in separate files</li>
<li>[*] Platform model</li>
<li>[*] Two feature models</li>
<li class="fragment cursor">[*] Documentation and reports</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

A component carries its documentation, so the build can produce the documents and reports of every variant.

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
<li>[*] Component model</li>
<li>[*] One product, several platforms</li>
<li>[*] A new platform leaves the products unchanged</li>
<li>[*] Product and platform choices in separate files</li>
<li>[*] Platform model</li>
<li>[*] Two feature models</li>
<li>[*] Documentation and reports</li>
<li class="fragment cursor">[*] Models as data</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Models as data: tools read them without running the build.

---

<p class="label">// one command per cell</p>

<div class="stage">
<div class="card abs disco" style="left:0; top:112px; width:150px;"><b>Disco</b></div>
<div class="card abs sleep" style="left:0; top:242px; width:150px;"><b>Sleep</b></div>
<div class="col-head abs" style="left:200px; top:30px; width:210px;">zephyr_esp32h2<small>prototype</small></div>
<div class="col-head abs" style="left:430px; top:30px; width:210px;">autosar<small>series product</small></div>
<div class="col-head abs" style="left:660px; top:30px; width:210px;">gtest<small>unit tests</small></div>
<div class="cell abs done cmd fragment" style="left:200px; top:100px; width:210px;" data-fragment-index="0">✓</div>
<div class="cell abs done cmd fragment" style="left:200px; top:230px; width:210px;" data-fragment-index="0">✓</div>
<div class="cell abs done cmd fragment" style="left:430px; top:100px; width:210px;" data-fragment-index="1">✓</div>
<div class="cell abs done cmd fragment" style="left:430px; top:230px; width:210px;" data-fragment-index="1">✓</div>
<div class="cell abs done cmd fragment" style="left:660px; top:100px; width:210px;" data-fragment-index="2">✓</div>
<div class="cell abs done cmd fragment" style="left:660px; top:230px; width:210px;" data-fragment-index="2">✓</div>
<div class="term abs fragment" style="left:0; top:350px; width:836px;" data-fragment-index="3">
<div class="head">terminal</div>
<div>$ yanga run --variant Disco --platform zephyr_esp32h2</div>
</div>
</div>

Note:

The grid from chapter 3, filled. Every cell is one command with a variant and a platform. The command is real for zephyr_esp32h2 and gtest; autosar is the what-if.

---

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="done">Just port it?</li>
<li class="done">What if: one product line, three platforms</li>
<li class="now">Three tools, side by side</li>
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>The same product line in Zephyr, spl-core and yanga.</p>
</div>
</div>

Note:

Chapter 7: Three tools, side by side. Say the sentence and go on.

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

<p class="label">// the thread</p>

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="done">Just port it?</li>
<li class="done">What if: one product line, three platforms</li>
<li class="done">Three tools, side by side</li>
<li class="now">Back to the start</li>
</ol>
<div class="thread-text">
<p>Back to the manager and the sentence from the start.</p>
</div>
</div>

Note:

Chapter 8: Back to the start. Say the sentence and go on.

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
