
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

A Zephyr project has two parts. The software components: kernel, drivers, subsystems such as shell and logging, and the vendor HAL as a module. And the tooling: west fetches the repositories and runs the build, CMake builds, Kconfig and devicetree configure, the SDK compiles, Twister runs the tests.

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
│   ├── <span class="w fragment mark c-disco" data-fragment-index="6">Disco</span>/
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
<div>$ ./build.sh <span class="fragment" data-fragment-index="3">--build</span> <span class="fragment" data-fragment-index="4">--variant</span> <span class="fragment" data-fragment-index="5"><span class="w fragment mark c-disco" data-fragment-index="6">Disco</span></span></div>
</div>
</div>

Note:

A variant is a folder with its name. config.txt holds the feature selection, parts.cmake lists the components of this variant. No board options in the selection, unlike prj_disco.conf. A third file, config.cmake, picks the toolchain. The command: build.sh hands the name to CMake as -DVARIANT=Disco, and CMakeLists.txt includes variants/${VARIANT}/config.cmake. Like FILE_SUFFIX in Zephyr, a CMake define picks the variant. The real config.txt also holds a few build settings such as the name of the output file.

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
<div class="code abs fragment" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f blk">components/light_controller/CMakeLists.txt</span><span class="blk"><span class="fragment hl-current">spl_add_source</span>(src/light_controller.c)</span><span class="blk"><span class="fragment hl-current">spl_add_test_source</span>(test/test_light_controller.cc)</span><span class="blk"><span class="fragment hl-current">spl_add_required_interface</span>(components/rte)</span><span class="blk"><span class="fragment hl-current">spl_create_component</span>(LONG_NAME "Light Controller")</span></div>
</div>

Note:

A component is a folder with its sources, its unit tests, its documentation and its own options, and a CMakeLists.txt that declares them with spl-core functions. One click per line: the production source, the test source, the interface it needs from another component, and the call that creates the component with a readable name. Compare chapter 3: there a component was a line in a list of sources.

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

All three come in unticked, then all three get ticked. spl-core has a variant model and a component model. They live in CMake files that only the build reads.

---

<p class="label">// unit tests</p>

<div class="stage">
<div class="tile abs" style="left:0; top:30px;">light_controller.c</div>
<span class="arrow abs fragment" style="left:196px; top:30px;" data-fragment-index="0">+</span>
<div class="tile abs fragment" style="left:230px; top:30px; width:240px;" data-fragment-index="0">test_light_controller.cc</div>
<span class="arrow abs fragment" style="left:486px; top:30px;" data-fragment-index="1">+</span>
<div class="tile mock abs fragment" style="left:520px; top:30px;" data-fragment-index="1">mocks for rte</div>
<div class="tile-note abs fragment" style="left:520px; top:82px;" data-fragment-index="1">generated by hammocking</div>
<div class="verdict abs fragment" style="left:0; top:120px;" data-fragment-index="2">= one test executable for light_controller</div>
<div class="term abs fragment" style="left:0; top:190px; width:836px; font-size:13px; white-space:nowrap;" data-fragment-index="3">
<div class="head">terminal</div>
<div>$ ./build.sh --build --variant Disco <span class="fragment" data-fragment-index="4">--build-kit test</span> <span class="fragment" data-fragment-index="5">--target components_light_controller_unittests</span></div>
<div class="fragment" data-fragment-index="6">$ ./build.sh --build --variant Disco --build-kit test --target unittests</div>
</div>
</div>

Note:

What goes into one unit test: the production source of the component, its test source, and mocks for everything the component calls from other components, here the RTE. The mocks are not written by hand: hammocking generates them. The result is one test executable per component, built and run on the host PC. Select the test build kit and build the unittests target of one component, or unittests for all components of the variant.

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
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”</div>
</div>

Note:

Section 4, about 2 minutes. Say it like the manager, who really believes it is a piece of cake. And it should be: that is the goal of this talk. Pause. Ask the room what they would do.

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:0; top:-20px; font-size:44px;" data-id="just">“Just port it.”</div>
<div class="app abs" style="left:0; top:70px;" data-id="app"><b>Application</b><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="layer abs zephyr" style="left:0; top:220px; width:400px;" data-id="m-zephyr">Zephyr</div>
<div class="layer abs board" style="left:0; top:286px; width:400px;" data-id="m-dev">Dev board</div>
<div class="layer abs autosar" style="left:460px; top:220px; width:400px;" data-id="m-autosar">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:460px; top:286px; width:400px;" data-id="m-series">Series board, in-house</div>
</div>

Note:

This is how "just port it" looks from the manager's desk. The application is one block.

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:0; top:-20px; font-size:44px;" data-id="just">“Just port it.”</div>
<div class="app abs" style="left:460px; top:70px;" data-id="app"><b>Application</b><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="layer abs zephyr ghost" style="left:0; top:220px; width:400px;" data-id="m-zephyr">Zephyr</div>
<div class="layer abs board ghost" style="left:0; top:286px; width:400px;" data-id="m-dev">Dev board</div>
<div class="layer abs autosar" style="left:460px; top:220px; width:400px;" data-id="m-autosar">AUTOSAR + RTE</div>
<div class="layer abs board series" style="left:460px; top:286px; width:400px;" data-id="m-series">Series board, in-house</div>
<div class="verdict abs" style="left:460px; top:360px;">Just move it over.</div>
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

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The platform leaves, and the red tiles leave with it. The holes are the work.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="tangled" -->

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
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Two requirements from the manager's request. The manager wants one product on two platforms. The red tiles show the opposite of the second one: the new platform changed the product.

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
<li>Back to the start</li>
</ol>
<div class="thread-text">
<p>The two teams sit at one table: can one repository build all three?</p>
</div>
</div>

Note:

Chapter 6: What if. The prototype team and the series team sit together. Say the sentence and go on.

---

<p class="label">// the question</p>

<div class="stage">
<div class="term abs fragment" style="left:0; top:110px; width:836px;" data-fragment-index="0">
<div class="head">terminal</div>
<div>$ … --variant Disco --platform zephyr</div>
<div class="fragment" data-fragment-index="1">$ … --variant Disco --platform autosar</div>
<div class="fragment" data-fragment-index="2">$ … --variant Disco --platform gtest</div>
</div>
</div>

Note:

The question the two teams ask: can one repository build Disco for all three? Zephyr for the prototype on the dev board, AUTOSAR for the series product, gtest for the unit tests on the host. One line per click. Only the platform name changes. Do not answer yet.

---

<p class="label">// the product line is in the build files</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:400px; font-size:16px;"><span class="f">Zephyr: app/CMakeLists.txt</span>
target_sources_ifdef(
    <span class="w fragment mark c-common" data-fragment-index="0">CONFIG_MANUAL_DIMMING</span>
    app PRIVATE
    src/brightness_controller.c)</div>
<div class="code abs" style="left:440px; top:20px; width:400px; font-size:16px;"><span class="f">spl-core: CMakeLists.txt</span>
include(variants/<span class="w fragment mark c-common" data-fragment-index="1">${VARIANT}</span>/config.cmake)
<span class="f">variants/Disco/parts.cmake</span>
<span class="w fragment mark c-common" data-fragment-index="1">spl_add_component</span>(
    components/light_controller)</div>
<div class="verdict abs fragment" style="left:0; top:260px;" data-fragment-index="2">Both build with CMake, and the product line lives inside the build files.</div>
</div>

Note:

The room has seen both files. First click: in Zephyr, a feature decides in CMake which sources are built. Second click: in spl-core, the variant is a CMake define, and the component list of a variant is CMake code. Both tools build with CMake, and in both the product line logic sits in the build files. Only the build can read it, and only this build.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios6" -->

<p class="label">// the idea</p>

<div class="stage">
<div class="zbox abs fragment" style="left:0; top:60px; width:200px;" data-fragment-index="0">product line data<div class="zrow"><span class="chip">features</span></div><div class="zrow"><span class="chip">variants</span></div><div class="zrow"><span class="chip">components</span></div></div>
<span class="arrow abs fragment" style="left:250px; top:110px;" data-fragment-index="1">→</span>
<div class="zbox abs fragment" style="left:290px; top:60px; width:180px;" data-fragment-index="1">generator<div class="zrow"><span class="chip">one per platform</span></div></div>
<span class="arrow abs fragment" style="left:518px; top:40px;" data-fragment-index="2">→</span>
<span class="arrow abs fragment" style="left:518px; top:170px;" data-fragment-index="2">→</span>
<div class="zbox abs fragment" style="left:560px; top:0; width:240px;" data-fragment-index="2">CMake glue<div class="zrow"><span class="chip">Zephyr build</span></div></div>
<div class="zbox abs fragment" style="left:560px; top:130px; width:240px;" data-fragment-index="2">CMake glue<div class="zrow"><span class="chip">series build</span></div></div>
<div class="verdict abs fragment" style="left:0; top:245px; font-size:20px; white-space:nowrap;" data-fragment-index="3">The steps differ, so <span class="fragment emph" data-fragment-index="4">the platform knows how to build a variant.</span></div>
</div>

<div class="notify fragment" data-id="bios" data-fragment-index="5"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The idea: take the product line out of the build files. First click: the features, the variants and the components as data, in a format that no build tool owns. Second click: a generator per platform reads that data. Third click: it writes the CMake glue that starts a Zephyr build, or the series build. Then the sentence, and click again for its second half: the steps differ per platform, so the platform knows how to build a variant. Nobody writes CMake for the variants and components; the platform's generators write it. The Zephyr platform of the open SPLed repository still has two small hand-written glue files.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="bios6" -->

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
<li class="fragment cursor">[*] SPL model data files</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

The product line models are data files. Any tool can read them, and a generator turns them into a build.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

<p class="label">// one product line, three platforms</p>

<div class="stage">
<div class="code abs" style="left:0; top:0; width:760px; font-size:18px;" data-id="ytree">SPLed/
├── <span class="hl">yanga.yaml</span>             <span class="f"># the pipeline and the feature model</span>
├── KConfig                <span class="f"># the product features</span>
├── variants/
│   ├── Disco/<span class="hl">yanga.yaml</span>
│   └── Sleep/<span class="hl">yanga.yaml</span>
├── components/
│   └── <span class="hl">yanga.yaml</span>         <span class="f"># all components</span>
└── platforms/
    ├── zephyr/<span class="hl">yanga.yaml</span>
    ├── autosar/<span class="hl">yanga.yaml</span>  <span class="f"># the what-if</span>
    └── gtest/<span class="hl">yanga.yaml</span></div>
<div class="verdict abs fragment" style="left:0; top:370px;">yanga reads every yanga.yaml, wherever it is.</div>
</div>

Note:

The what-if, built with yanga. One repository, one application, three platforms. The data lives in yanga.yaml files, and yanga collects all of them, in any folder. The folders are SPLed's choice, not a rule: SPLed keeps all its components in one file. The zephyr and gtest platforms exist in the open SPLed repository; the autosar platform is the what-if.

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
    file: variants/Disco/config.txt</div>
</div>

Note:

The variant is data: its name, a description, its components and its feature selection. The same model as in spl-core, written as YAML instead of CMake. SPLed puts each variant in its own folder; yanga does not require it.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

<p class="label">// where is the component model?</p>

<div class="stage">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="ytree">SPLed/
├── yanga.yaml
├── KConfig
├── variants/
├── components/
│   ├── <span class="hl">yanga.yaml</span>
│   └── light_controller/
└── platforms/</div>
<div class="code abs" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f blk">components/yanga.yaml (abridged)</span><span class="blk">components:
- name: light_controller</span><span class="fragment hl-current blk">  path: components/light_controller</span><span class="fragment hl-current blk">  docs_sources:
  - doc/index.md</span><span class="fragment hl-current blk">  sources:
  - src/light_controller.c</span><span class="fragment hl-current blk">  testing:
    sources:
    - test/test_light_controller.cc</span><span class="fragment hl-current blk">  required_components:
  - rte</span></div>
<div class="verdict abs fragment" style="left:0; top:370px;">No CMake for it: the platform writes the build.</div>
</div>

Note:

The real light_controller entry of the yanga port of SPLed, shortened. One click per part: the folder, the documentation, the production source, the test source, and the component it needs. The same component model as in spl-core, as data instead of CMake functions. Last click: nobody writes CMake for the component; the platform's generator writes it.

---

<p class="label">// where is the platform model?</p>

<div class="stage">
<div class="pipe abs fragment" style="left:0px; top:0;" data-fragment-index="0">
<div class="col-head" style="width:270px;">zephyr<small>prototype</small></div>
<div class="pstep">Install riscv64-zephyr-elf</div>
<div class="pstep">Fetch Zephyr and its modules: west</div>
<div class="pstep shared">Generate the feature header</div>
<div class="pstep">Generate CMake for the variant</div>
<div class="pstep build">west build</div>
</div>
<div class="pipe abs fragment" style="left:305px; top:0;" data-fragment-index="1">
<div class="col-head" style="width:270px;">autosar<small>series product</small></div>
<div class="pstep">Install the compiler</div>
<div class="pstep">Fetch BSW and MCAL</div>
<div class="pstep">Configure the BSW: ARXML</div>
<div class="pstep">Generate RTE and BSW code</div>
<div class="pstep shared">Generate the feature header</div>
<div class="pstep build">Build</div>
</div>
<div class="pipe abs fragment" style="left:610px; top:0;" data-fragment-index="2">
<div class="col-head" style="width:270px;">gtest<small>unit tests</small></div>
<div class="pstep">Install gcc</div>
<div class="pstep">Fetch GoogleTest</div>
<div class="pstep shared">Generate the feature header</div>
<div class="pstep">Generate the tests and mocks</div>
<div class="pstep build">Build and run the tests</div>
</div>
<div class="verdict abs fragment" style="left:0; top:365px;" data-fragment-index="3">A platform brings its own tools and its own components.</div>
</div>

Note:

Each platform brings its own pipeline: the steps that must run before its build. One column per click. Zephyr and gtest are the real pipelines of the yanga port of SPLed; the autosar column is the what-if. Only one step is the same on all three: the header with the product features, generated from the product feature model. Everything else belongs to the platform. Last click: a platform brings its own tools and its own components, such as the adapters to the drivers.

---

<p class="label">// a platform definition</p>

<div class="stage">
<div class="code abs" style="left:60px; top:0; width:720px; font-size:15px;"><span class="f blk">platforms/zephyr/yanga.yaml (abridged)</span><span class="blk">platforms:
- name: zephyr_esp32h2
  description: Zephyr on the ESP32-H2 devkit</span><span class="fragment hl-current blk">  feature_model:
    file: KConfig</span><span class="fragment hl-current blk">  components: [platform_types, zephyr_adapters, zephyr_led_ws2812]</span><span class="fragment hl-current blk">  configs:
    - id: west
      file: platforms/zephyr/west.yaml
    - id: poks
      file: platforms/zephyr/poks.json</span><span class="fragment hl-current blk">  pipeline:
    - include: pipeline/zephyr.yaml
    - step: FetchEspressifBlobs
    - step: ZephyrBuild
      config:
        board: esp32h2_devkitm/esp32h2</span><span class="fragment hl-current blk">  build_targets: [all, flash, report]</span></div>
</div>

Note:

The real definition of the zephyr_esp32h2 platform in the yanga port of SPLed, shortened. One click per part. feature_model: the platform's own features, Zephyr's Kconfig tree, kept apart from the product features. components: the components only this platform has, such as the Zephyr adapters for the LED and the buttons. configs: which Zephyr and which modules, in a west manifest, and which toolchain, from poks. pipeline: the steps before the build and the build itself, with the board. build_targets: what can be built on this platform, for example flash. The variant appears nowhere in it.

---

<!-- .slide: data-background-color="#0000a8" -->

<div class="mc">
<div class="mc-top">.config - yanga as a development environment for a product line</div>
<div class="mc-box">
<div class="mc-title">Requirements</div>
<div class="mc-help">What yanga gives the product line.</div>
<ul class="mc-list">
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="1">*</span>] Feature model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="1">Kconfig, as in Zephyr and spl-core</span></li>
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="2">*</span>] Variant model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="2">data in yanga.yaml</span></li>
<li class="fragment" data-fragment-index="0">[<span class="fragment" data-fragment-index="3">*</span>] Component model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="3">data in yanga.yaml, the platform writes the CMake</span></li>
<li class="fragment" data-fragment-index="4">[<span class="fragment" data-fragment-index="5">*</span>] Platform model&nbsp;&nbsp;<span class="why fragment" data-fragment-index="5">tools, pipeline and components as data</span></li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

The same three rows as for Zephyr and spl-core, and all three get ticked. Then a fourth row appears: the platform model. Zephyr is a platform and spl-core builds for one platform, so neither needed this row. Here the platform is a model of its own: its tools, its pipeline and its components. The variant does not change when the platform changes. The zephyr_esp32h2 and gtest platforms are real; autosar is the what-if.

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
<li class="now">Back to the start</li>
</ol>
<div class="thread-text">
<p>Back to the manager and the sentence from the start.</p>
</div>
</div>

Note:

Chapter 8: Back to the start. Say the sentence and go on.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios8" -->

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
<div class="code"><span class="f">variants/Disco/zephyr_esp32h2.txt</span>
<span class="f"># Disco's Zephyr selection</span>
<span class="f"># for the ESP32-H2</span></div>
</div>
</div>

<div class="notify fragment" data-id="bios" style="right:290px; bottom:-170px;"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The same variant in three tools, as the files show it. One column per click. Zephyr keeps the board options and the product features in one file, prj_disco.conf. spl-core and yanga keep the product features in config.txt. yanga keeps Disco's options for the Zephyr board in a file of their own. Today the file holds only its comment, because Disco uses the board defaults.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="bios8" -->

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
<li>[*] SPL model data files</li>
<li>[*] Platform model</li>
<li class="fragment cursor">[*] Product and platform choices in separate files</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

The product team owns the product features, the platform team owns the board options. Each selection lives in its own file.

---

<!-- .slide: data-auto-animate data-auto-animate-id="close" -->

<div class="stage">
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”</div>
<div class="verdict abs fragment" style="left:110px; top:290px; font-size:40px;">“There is nothing to port.”</div>
<div class="verdict abs fragment" style="left:110px; top:360px; width:700px;">Both platforms and their builds live in the same repository. Pick the variant and the platform.</div>
</div>

Note:

Section 8, about 2 minutes. The opening line comes back. This time it really is a piece of cake: there is nothing to port. The prototype platform and the series platform, and how each one builds, live in the same repository as the product line. Building for the series board means picking the variant and the platform.

---

<!-- .slide: data-background-color="#0000a8" -->

<div class="mc">
<div class="mc-top">.config - development environment for a product line</div>
<div class="mc-box">
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
<li>[*] R10 SPL model data files</li>
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

---

### Backup

Note:

Backup slides, for questions only.

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

Every cell is one command with a variant and a platform. The command is real for zephyr_esp32h2 and gtest; autosar is the what-if.
