
## There Is More to a Product Line Than Zephyr Boards

Asking the SPLE Question First

<hr>

ESE Kongress 2026 in Sindelfingen <!-- .element: class="ese-event" -->

<div class="ese-logos">
<img src="../images/RMT-Logo_TransparentBG.png" alt="RMT logo">
<img src="../images/Marquardt-100-Years-Keyvisual-white-gold.png" alt="Marquardt logo">
</div>

Note:

Welcome. The talk is about software product line engineering, Zephyr boards and other open source tools for building product lines.

---

### Who am I?

<div class="speakers">
<div class="speaker">

Alexandru

</div>
</div>

Note:

Who I am, in one sentence: a software engineer.

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

I started when websites looked like this. Embedded engineering, build systems and test frameworks since then. My current projects are on maxiniuc.com.

---

<div class="thread">
<ol class="rail">
<li class="now">Two customers, one product line</li>
<li>From wishes to features</li>
<li>A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>We follow one product line from the first customer e&#8209;mail to the series product.</p>
<p>Along the way, we collect what the development environment needs.</p>
</div>
</div>

Note:

The thread: we follow one product line from the first customer e-mail to series production, and collect what the development environment needs on the way.

---

### Context

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
<div class="lead abs" style="left:0; top:0; width:880px;">We are a supplier. We build SPLed, a small light controller, for two customers.</div>
<div class="customer abs" style="left:80px; top:220px;">Customer A</div>
<div class="customer abs" style="left:500px; top:220px;">Customer B</div>
<div class="wall abs fragment" style="left:438px; top:200px;"></div>
</div>
</div>

Note:

We are a supplier and build a small light controller, SPLed, for two customers who do not know about each other. Click: the wall between them.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="now">From wishes to features</li>
<li>A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>Two customers write what they want.</p>
</div>
</div>

Note:

We start with two customer e-mails and try to understand what each one wants.

---

<!-- .slide: data-auto-animate data-auto-animate-id="fm" -->

### Customer input

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:54px; width:880px;">
<div class="msg abs" style="left:0; top:10px;">
<div class="msg-head">From: Customer A<br>Subject: light for our party room</div>
<p>We need a <span class="w fragment mark c-common" data-fragment-index="0">light</span> for our party room. It shall <span class="w fragment mark c-disco" data-fragment-index="1" data-id="blink">blink</span> so people notice it. Please make it <span class="w fragment mark c-disco" data-fragment-index="1" data-id="green">green</span>. We want to <span class="w fragment mark c-common" data-fragment-index="0">switch it on and off</span> with one button.</p>
</div>
<div class="msg abs" style="left:460px; top:70px;">
<div class="msg-head">From: Customer B<br>Subject: bedroom lights</div>
<p>Our hotel needs a calm <span class="w fragment mark c-common" data-fragment-index="0">light</span> for the bedrooms. Guests shall <span class="w fragment mark c-sleep" data-fragment-index="1" data-id="dim">dim it by hand</span>. A soft <span class="w fragment mark c-sleep" data-fragment-index="1" data-id="purple">purple</span> works best. And of course a button to <span class="w fragment mark c-common" data-fragment-index="0">switch it on and off</span>.</p>
</div>
</div>
</div>

Note:

Click 1: what both want, a light that switches on and off. Click 2: what differs, green and blinking for A, purple and dimmable for B.

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

The differences become features, and each customer gets a variant: Disco for A, Sleep for B. The round brackets mean pick one.

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

First requirements: model features and model variants, so that customer, system engineers and software engineers can see and discuss them.

---

<!-- .slide: data-auto-animate data-auto-animate-id="concerns" -->

### Separation of concerns

<div class="stage">
<!-- The content is 315px high: this offset centres it in the stage. -->
<div class="abs" style="left:0; top:108px; width:880px;">
<p class="label abs fragment" style="left:0; top:-30px;" data-fragment-index="0">// wishes</p>
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
</div>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

To reason about the product, separate the concerns. Click 1: the wishes. Click 2: the components, such as light_controller and power_button. Features and components are not one to one.

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

New requirement: model components, the parts you split the functionality into.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="now">A prototype on Zephyr</li>
<li>The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>We know the features, the variants and the components. Now they have to run on a board.</p>
</div>
</div>

Note:

We know the features, the variants and the components. Now they have to run on a board.

---

### The decision

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:88px; width:880px;">
<div class="msg abs" style="left:78px; top:40px; width:680px;">
<div class="msg-head">From: Innovation team<br>Subject: prototypes for Disco and Sleep</div>
<p>We build the prototypes on the <span class="w fragment mark c-common">ESP32-H2 dev board</span> with <span class="w fragment mark c-common">Zephyr</span>. Drivers, shell and logging come with it, so the board runs <span class="w fragment mark c-common">within days</span>.</p>
</div>
</div>
</div>

Note:

The innovation team builds the prototype on an ESP32 board with Zephyr. It runs within days.

---

### What Zephyr brings

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:118px; width:880px;">
<div class="zbox abs" style="left:0; top:20px; width:380px;">Software components<div><span class="chip">Kernel</span><span class="chip">Device drivers</span><span class="chip">Shell</span><span class="chip">Logging</span><span class="chip">HAL modules</span></div></div>
<div class="zbox abs fragment" style="left:446px; top:20px; width:380px;">Tooling and build environment<div><span class="chip">west</span><span class="chip">CMake</span><span class="chip">Kconfig</span><span class="chip">devicetree</span><span class="chip">Zephyr SDK</span><span class="chip">Twister</span></div></div>
<div class="verdict abs fragment" style="left:0; top:180px;">The team takes both: the code and the way of working.</div>
</div>
</div>

Note:

Zephyr brings software components (kernel, drivers, shell, logging) and tooling (west, CMake, Kconfig). The team takes both.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zapp" -->

### The first application

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
<div class="code abs" style="left:0; top:20px; width:700px; font-size:22px;" data-id="tree">app/
├── CMakeLists.txt   <span class="f"># finds Zephyr, lists the sources</span>
├── Kconfig          <span class="f"># the SPLed features</span>
├── prj.conf         <span class="f"># the selection for this build</span>
└── src/             <span class="f"># the SPLed components</span></div>
</div>
</div>

Note:

A Zephyr application is a small folder. The pattern for every environment today: where is the feature model, the variant model, the component model?

---

<!-- .slide: data-auto-animate data-auto-animate-id="zapp" -->

### Where is the feature model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
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
</div>

Note:

The feature model is Kconfig: blinking and dimming as booleans, the color as a choice. Click 2: the last line pulls in all of Zephyr's own options.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zvar" -->

### Where is the variant model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
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
</div>

Note:

A variant is a prj_<name>.conf file; prj.conf is Zephyr's default name. One click per part of the command: the board, the app, and FILE_SUFFIX=disco picks the variant file.

---

### From the selection to the code

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:52px; width:880px;">
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
</div>

Note:

The build generates a header for the C code and a .config for CMake, so code and build differ per variant.

---

<!-- .slide: data-auto-animate data-auto-animate-id="zvar" -->

### Where is the component model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
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
</div>

Note:

The component model is CMakeLists.txt: a list of source files, some taken only for a feature.

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

Zephyr: feature model yes, variant model partly, component model no. CMake knows files and targets, not components.

---

### Debugging without the board

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:22px; width:880px;">
<div class="layer abs app-layer" style="left:40px; top:20px;">Application: SPLed components</div>
<div class="chip-test abs fragment" style="left:600px; top:28px;" data-fragment-index="1">+ ztest unit tests</div>
<div class="zbox abs" style="left:40px; top:96px;">Zephyr RTOS<div class="zrow"><span class="zk">Subsystems</span><span class="chip">Shell</span><span class="chip">Logging</span></div><div class="zrow"><span class="zk">Device drivers</span><span class="chip">GPIO</span><span class="chip">LED strip (WS2812)</span></div><div class="zrow"><span class="zk">Kernel</span><span class="chip">Threads</span><span class="chip">Timers</span></div></div>
<div class="layer abs board fragment fade-out" style="left:40px; top:290px;" data-fragment-index="0">ESP32-H2 dev board</div>
<div class="layer abs host fragment" style="left:40px; top:290px;" data-fragment-index="0">native_sim on the host PC</div>
<div class="verdict abs fragment" style="left:40px; top:370px;" data-fragment-index="1">Bugs are reproduced in unit tests on the host, not on the board.</div>
</div>
</div>

Note:

Change the board to native_sim and the same code runs on the host PC. Add ztest unit tests to debug without the board.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="now">The series product on AUTOSAR</li>
<li>Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>The business unit takes over: the same features and variants, a different platform.</p>
</div>
</div>

Note:

The business unit builds the series product: same features and variants, a different platform.

---

### The decision

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:88px; width:880px;">
<div class="msg abs" style="left:78px; top:40px; width:680px;">
<div class="msg-head">From: Business Unit Light<br>Subject: series development for Disco and Sleep</div>
<p>We build the series products on our <span class="w fragment mark c-common">in-house board</span> with <span class="w fragment mark c-common">AUTOSAR</span>. Our product lines are built with <span class="w fragment mark c-common">spl-core</span>, and the safety case needs a qualified stack.</p>
</div>
</div>
</div>

Note:

The business unit uses its in-house board, AUTOSAR and spl-core, an open source SPL build environment.

---

### What the series platform brings

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:90px; width:880px;">
<div class="zbox abs" style="left:0; top:20px; width:380px;">Software components<div><span class="chip">OS</span><span class="chip">RTE</span><span class="chip">COM</span><span class="chip">I/O hardware abstraction</span><span class="chip">MCAL</span></div></div>
<div class="zbox abs fragment" style="left:446px; top:20px; width:380px;">Tooling and build environment<div><span class="chip">Vendor configurator</span><span class="chip">ARXML</span><span class="chip">RTE generator</span><span class="chip">spl-core</span><span class="chip">CMake</span><span class="chip">Kconfig</span><span class="chip">GoogleTest</span></div></div>
<div class="verdict abs fragment" style="left:0; top:200px;">Again both: the code and the way of working. None of it is Zephyr's.</div>
</div>
</div>

Note:

The series platform brings the AUTOSAR basic software and its own tooling: RTE generator, spl-core, Kconfig, GoogleTest. None of it is Zephyr's.

---

<!-- .slide: data-auto-animate data-auto-animate-id="sapp" -->

### The first series application

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:28px; width:880px;">
<div class="code abs" style="left:0; top:20px; width:700px; font-size:22px;" data-id="stree">SPLed/
├── CMakeLists.txt   <span class="f"># includes spl-core</span>
├── KConfig          <span class="f"># the SPLed features</span>
├── variants/        <span class="f"># one folder per variant</span>
└── components/      <span class="f"># one folder per component</span></div>
</div>
</div>

Note:

The spl-core project is also a small folder. Same three questions.

---

<!-- .slide: data-auto-animate data-auto-animate-id="sapp" -->

### Where is the feature model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:28px; width:880px;">
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
</div>

Note:

The feature model is Kconfig again, with the same features as in Zephyr.

---

<!-- .slide: data-auto-animate data-auto-animate-id="svar" -->

### Where is the variant model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:26px; width:880px;">
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
</div>

Note:

A variant is a folder: config.txt holds the selection, parts.cmake lists the components. One click per part of the command: build.sh --build --variant Disco.

---

<!-- .slide: data-auto-animate data-auto-animate-id="svar" -->

### Where is the component model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:26px; width:880px;">
<div class="code abs" style="left:0; top:20px; width:270px; font-size:16px;" data-id="stree">components/
└── light_controller/
    ├── <span class="hl">CMakeLists.txt</span>
    ├── KConfig
    ├── src/
    ├── test/
    └── doc/</div>
<div class="code abs fragment" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f blk">components/light_controller/CMakeLists.txt</span><span class="blk"><span class="fragment hl-current">spl_add_source</span>(src/light_controller.c)</span><span class="blk"><span class="fragment hl-current">spl_add_test_source</span>(test/test_light_controller.cc)</span><span class="blk"><span class="fragment hl-current">spl_add_required_interface</span>(components/rte)</span><span class="blk"><span class="fragment hl-current">spl_create_component</span>(LONG_NAME "Light Controller")</span></div>
</div>
</div>

Note:

A component is a folder with a CMakeLists.txt that declares its sources, tests and dependencies with spl-core functions. One click per line.

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

spl-core: feature, variant and component model, all ticked. They live in CMake files.

---

### Unit tests

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:74px; width:880px;">
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
</div>

Note:

A component with a test gets its unit test target automatically, with generated mocks. The target name is the component path with underscores. unittests builds all of them.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="now">Just port it?</li>
<li>What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>The series product runs on another platform. How hard can the move be?</p>
</div>
</div>

Note:

Two environments, one application. How hard can the move be?

---

<!-- .slide: data-auto-animate data-auto-animate-id="just" -->

<div class="stage">
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”</div>
</div>

Note:

Say it like someone who believes it: "Just port it."

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

From the outside, the application is one block.

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

Pick it up, put it down. No issues, it seems.

---

<!-- .slide: data-auto-animate data-auto-animate-id="tangled" -->

### What is inside the block

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

With a good architecture, only the red components call the platform.

---

<!-- .slide: data-auto-animate data-auto-animate-id="tangled" -->

### Just port it

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
<div class="verdict abs" style="left:40px; top:310px; white-space:nowrap;">Port = rewrite every red tile.<span class="fragment"> Known cure: a thin adapter.</span></div>
<div class="tile abs tied ghost" style="left:60px; top:370px;" data-id="t5">power_button</div>
<div class="tile abs tied ghost" style="left:260px; top:370px;" data-id="t6">led_interface</div>
<div class="tile abs tied ghost" style="left:460px; top:370px;" data-id="t7">button_interface</div>
<div class="layer abs zephyr ghost" style="left:40px; top:416px;" data-id="zephyr">Zephyr</div>
</div>

Note:

In theory, replace the red parts and the application runs on AUTOSAR. Give the room time to read. Click: the known cure, a thin adapter.

---

<!-- .slide: data-auto-animate data-auto-animate-id="move" -->

### And the build environment?

<table class="move">
<thead><tr><th></th><th>Zephyr</th><th>spl-core</th><th>The move</th></tr></thead>
<tbody>
<tr class="fragment"><td>Features</td><td><code>app/Kconfig</code></td><td><code>KConfig</code></td><td class="cost ok">same language: it carries over</td></tr>
<tr class="fragment"><td>Variants</td><td><code>prj_disco.conf</code></td><td><code>variants/Disco/</code><br><code>config.txt</code>, <code>parts.cmake</code></td><td class="cost">sort every line: product or board; write the component list</td></tr>
<tr class="fragment"><td>Components</td><td>one source list in <code>CMakeLists.txt</code></td><td>a folder per component</td><td class="cost">split the list, write a CMakeLists.txt each, find the dependencies</td></tr>
<tr class="fragment"><td>Tests</td><td>ztest on <code>native_sim</code></td><td>GoogleTest and mocks</td><td class="cost">rewrite every test</td></tr>
<tr class="fragment"><td>Build</td><td><code>west build</code></td><td><code>./build.sh</code></td><td class="cost">a new way of working</td></tr>
</tbody>
</table>

<p class="verdict fragment">Moving the code is the part you see. The product line is rebuilt in the new build environment.</p>

<div class="notify fragment" data-id="bios"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

The code is not the problem, the build environment is. One row per click: features carry over, variants, components, tests and the build do not. The product line is rebuilt in the new environment.

---

<!-- .slide: data-background-color="#0000a8" data-auto-animate data-auto-animate-id="move" -->

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

Critical requirements: one product on several platforms, and a new platform leaves the product unchanged.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="done">Just port it?</li>
<li class="now">What if: one product line, three platforms</li>
<li>Conclusion</li>
</ol>
<div class="thread-text">
<p>The two teams sit at one table: can one repository build all three?</p>
</div>
</div>

Note:

What if we designed such an environment?

---

### The question

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:42px; width:880px;">
<div class="term abs fragment" style="left:0; top:110px; width:836px;" data-fragment-index="0">
<div class="head">terminal</div>
<div>$ … --variant Disco --platform zephyr</div>
<div class="fragment" data-fragment-index="1">$ … --variant Disco --platform autosar</div>
<div class="fragment" data-fragment-index="2">$ … --variant Disco --platform gtest</div>
</div>
</div>
</div>

Note:

What we want: the same variant, only the platform name changes. One line per click: zephyr, autosar, gtest.

---

### The product line is in the build files

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:60px; width:880px;">
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
</div>

Note:

Today the product line lives in CMake, and CMake is a build system, not an SPL tool.

---

<!-- .slide: data-auto-animate data-auto-animate-id="bios6" -->

### The idea

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:74px; width:880px;">
<div class="node abs fragment" style="left:0; top:0; width:240px; height:240px;" data-fragment-index="0">product line<span class="chip">features</span><span class="chip">variants</span><span class="chip">components</span></div>
<div class="node abs fragment" style="left:580px; top:0; width:300px; height:100px;" data-fragment-index="1">CMake glue<span class="chip">Zephyr build</span></div>
<div class="node abs fragment" style="left:580px; top:140px; width:300px; height:100px;" data-fragment-index="1">CMake glue<span class="chip">series build</span></div>
<div class="node abs fragment" style="left:310px; top:70px; width:200px; height:100px;" data-fragment-index="2">generator<span class="chip">one per platform</span></div>
<svg class="flow abs fragment" style="left:0; top:0;" width="880" height="240" viewBox="0 0 880 240" data-fragment-index="2">
<defs><marker id="flow-head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" /></marker></defs>
<line x1="250" y1="120" x2="300" y2="120" marker-end="url(#flow-head)" />
<line x1="520" y1="105" x2="570" y2="55" marker-end="url(#flow-head)" />
<line x1="520" y1="135" x2="570" y2="185" marker-end="url(#flow-head)" />
</svg>
<div class="verdict abs fragment" style="left:0; top:280px; white-space:nowrap;" data-fragment-index="3">The steps differ, so <span class="fragment emph" data-fragment-index="4">the platform knows how to build a variant.</span></div>
</div>
</div>

<div class="notify fragment" data-id="bios" data-fragment-index="5"><div class="notify-head"><span>⚠ Development environment</span><span>✕</span></div><div class="notify-body"><b>New requirement detected</b>Your development environment does not meet it yet.</div><div class="notify-buttons"><span class="disabled">Remind me later</span><span class="primary">Open</span></div></div>

Note:

Describe the product line once and generate the CMake glue per platform. One click per box. The platform knows how to build; the product line does not care.

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

New requirement: the product line is described in data files, not in CMake.

---

### Which format?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:16px; width:880px;">
<div class="fragment" data-fragment-index="0">
<div class="fragment semi-fade-out" data-fragment-index="1">
<div class="code abs" style="left:0; top:0; width:380px; font-size:13px;">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;variants&gt;
  &lt;variant&gt;
    &lt;name&gt;Disco&lt;/name&gt;
    &lt;components&gt;
      &lt;component&gt;rte&lt;/component&gt;
      &lt;component&gt;spled&lt;/component&gt;
      &lt;component&gt;light_application&lt;/component&gt;
    &lt;/components&gt;
    &lt;feature_selection&gt;
      &lt;file&gt;variants/Disco/config.txt&lt;/file&gt;
    &lt;/feature_selection&gt;
  &lt;/variant&gt;
&lt;/variants&gt;</div>
</div>
</div>
<div class="scared abs fragment" style="left:166px; top:104px;" data-fragment-index="1">😱</div>
<div class="fragment" data-fragment-index="2">
<div class="fragment semi-fade-out" data-fragment-index="4">
<div class="code abs" style="left:452px; top:0; width:396px; font-size:13px;">{
  "variants": [{
    "name": "Disco",
    "components": [
      "rte", "spled", "light_application"
    ],
    "feature_selection": {
      "file": "variants/Disco/config.txt"
    }
  }]
}</div>
</div>
</div>
<div class="code abs fragment pick" style="left:452px; top:250px; width:396px; font-size:15px;" data-fragment-index="3">variants:
- name: Disco
  components: [rte, spled, light_application]
  feature_selection:
    file: variants/Disco/config.txt</div>
<div class="verdict abs fragment" style="left:0; top:400px;" data-fragment-index="4">Let's go with YAML.</div>
</div>
</div>

Note:

XML is too much to write, JSON is better, YAML is the shortest. This is what yanga uses: a build-system-agnostic way to describe an SPL, with generators for CMake.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

### Where is the variant model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:32px; width:880px;">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="ytree">SPLed/
├── yanga.yaml
├── KConfig
├── variants/
│   └── Disco/
│       ├── <span class="hl">yanga.yaml</span>
│       └── config.txt
├── components/
└── platforms/</div>
<div class="code abs bar-disco" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f blk">variants/Disco/yanga.yaml</span><span class="blk">variants:</span><span class="fragment hl-current blk">- name: Disco</span><span class="fragment hl-current blk">  description: The LED blinks and one can change ...</span><span class="fragment hl-current blk">  components: [rte, spled, light_application]</span><span class="fragment hl-current blk">  feature_selection:
    file: variants/Disco/config.txt</span></div>
</div>
</div>

Note:

A variant in yanga.yaml: name, description, components and feature selection. One click per part.

---

<!-- .slide: data-auto-animate data-auto-animate-id="yapp" -->

### Where is the component model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:32px; width:880px;">
<div class="code abs" style="left:0; top:20px; width:250px; font-size:16px;" data-id="ytree">SPLed/
├── yanga.yaml
├── KConfig
├── variants/
├── components/
│   ├── <span class="hl">yanga.yaml</span>
│   └── light_controller/
└── platforms/</div>
<div class="code abs" style="left:320px; top:20px; width:520px; font-size:16px;"><span class="f blk">components/yanga.yaml (abridged)</span><span class="blk">components:
- name: light_controller</span><span class="fragment hl-current blk">  docs:
  - doc/index.md</span><span class="fragment hl-current blk">  sources:
  - src/light_controller.c</span><span class="fragment hl-current blk">  testing:
  - test/test_light_controller.cc</span><span class="fragment hl-current blk">  required_components:
  - rte</span></div>
</div>
</div>

Note:

A component in yanga.yaml: docs, sources, tests and required components. The generators write the CMake. One click per part.

---

### Every platform builds its own way

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:34px; width:880px;">
<div class="pipe abs fragment" style="left:0px; top:0;" data-fragment-index="0">
<div class="col-head" style="width:270px;">zephyr<small>prototype</small></div>
<div class="pstep">Install riscv64-zephyr-elf</div>
<div class="pstep">Fetch Zephyr and its modules: west</div>
<div class="pstep">Generate the feature header</div>
<div class="pstep">Generate CMake for the variant</div>
<div class="pstep build">west build</div>
</div>
<div class="pipe abs fragment" style="left:305px; top:0;" data-fragment-index="1">
<div class="col-head" style="width:270px;">autosar<small>series product</small></div>
<div class="pstep">Install the compiler</div>
<div class="pstep">Fetch BSW and MCAL</div>
<div class="pstep">Configure the BSW: ARXML</div>
<div class="pstep">Generate RTE and BSW code</div>
<div class="pstep">Generate the feature header</div>
<div class="pstep build">Build</div>
</div>
<div class="pipe abs fragment" style="left:610px; top:0;" data-fragment-index="2">
<div class="col-head" style="width:270px;">gtest<small>unit tests</small></div>
<div class="pstep">Install gcc</div>
<div class="pstep">Fetch GoogleTest</div>
<div class="pstep">Generate the feature header</div>
<div class="pstep">Generate the tests and mocks</div>
<div class="pstep build">Build and run the tests</div>
</div>
<div class="verdict abs fragment" style="left:0; top:365px;" data-fragment-index="3">A platform brings its own tools and its own components.</div>
</div>
</div>

Note:

Every platform builds its own way. One column per click. The platform knows how to build a variant; the variant does not care.

---

### Where is the platform model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:82px; width:880px;">
<div class="code abs" style="left:60px; top:0; width:720px; font-size:15px;"><span class="f blk">platforms/zephyr/yanga.yaml (abridged)</span><span class="blk">platforms:
- name: zephyr_esp32h2
  description: Zephyr on the ESP32-H2 devkit</span><span class="fragment hl-current blk">  components: [platform_types, zephyr_adapters, zephyr_led_ws2812]</span><span class="fragment hl-current blk">  configs:
  - id: poks
    file: platforms/zephyr/poks.json</span><span class="fragment hl-current blk">  pipeline:
    - include: pipeline/zephyr.yaml
    - step: FetchEspressifBlobs
    - step: ZephyrBuild
      config:
        board: esp32h2_devkitm/esp32h2</span></div>
</div>
</div>

Note:

The platform model: its components, its tools (poks installs them) and its pipeline. One click per part.

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

Now four models: feature, variant and component belong to the product; the platform is what you build for.

---

<div class="thread">
<ol class="rail">
<li class="done">Two customers, one product line</li>
<li class="done">From wishes to features</li>
<li class="done">A prototype on Zephyr</li>
<li class="done">The series product on AUTOSAR</li>
<li class="done">Just port it?</li>
<li class="done">What if: one product line, three platforms</li>
<li class="now">Conclusion</li>
</ol>
<div class="thread-text">
<p>What a new platform costs now, and the answer to “Just port it.”</p>
</div>
</div>

Note:

Conclusion.

---

### Adding a platform

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:40px; width:880px;">
<div class="code abs" style="left:0; top:0; width:500px; font-size:18px;">SPLed/
├── variants/      <span class="f"># unchanged</span>
├── components/    <span class="f"># unchanged</span>
└── platforms/
    ├── zephyr/
    ├── autosar/   <span class="f"># the what-if</span>
    ├── gtest/
    └── <span class="w fragment mark c-common" data-fragment-index="0">tc375/</span><span class="fragment" data-fragment-index="0">     <span class="f"># new</span></span></div>
<div class="term abs fragment" style="left:0; top:290px; width:836px;" data-fragment-index="1">
<div class="head">terminal</div>
<div>$ yanga run --variant Disco --platform tc375</div>
</div>
</div>
</div>

Note:

Adding a platform is a new folder; the product stays as it is. Click: tc375. Click: the same variant, built for it. TC375 is a bare-metal TriCore build without AUTOSAR.

---

<!-- .slide: data-auto-animate data-auto-animate-id="close" -->

<div class="stage">
<div class="just abs" style="left:110px; top:150px;" data-id="just">“Just port it.”</div>
<div class="verdict abs fragment" style="left:110px; top:320px; font-size:40px;">“There is nothing to port.”</div>
<div class="verdict abs fragment" style="left:110px; top:395px; width:700px;">All platforms and their builds live in the same repository. Pick the variant and the platform.</div>
</div>

Note:

"Just port it." Click: there is nothing to port. Click: all platforms live in the same repository as the product line.

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
<li>[*] R4 Feature model</li>
<li>[*] R5 Variant model</li>
<li>[*] R6 Platform model</li>
<li>[*] R7 Component model</li>
<li>[*] R10 SPL model data files</li>
<li>&nbsp;&nbsp;&nbsp; R3, R8, R9 ---&gt; in the article</li>
</ul>
<div class="mc-buttons"><span class="sel">&lt;Select&gt;</span><span>&lt; Exit &gt;</span><span>&lt; Help &gt;</span><span>&lt; Save &gt;</span><span>&lt; Load &gt;</span></div>
</div>
</div>

Note:

Take a photo and check your own development environment against this list. The article has the details.

---

### Questions?

<div class="qr">

![QR code of the slides](../images/qr_zephyr_meets_sple.png)

</div>

https://avengineers.github.io/ESE-2026/docs/zephyr_meets_sple/ <!-- .element: class="deck-url" -->

Note:

Thank you for your attention. Open for questions.

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

### With a thin shell

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

### Just port it, again

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

### The same light, four altitudes

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:68px; width:880px;">
<div class="step l1 abs" style="left:0; top:0;"><small>customer · sales</small>“A green light that blinks.”</div>
<div class="step l2 abs fragment" style="left:120px; top:110px;"><small>product features · system engineer</small>BLINKING=y &nbsp; COLOR_GREEN=y</div>
<div class="step l3 abs fragment" style="left:240px; top:210px;"><small>platform features · software engineer</small>WS2812_STRIP_SPI=y</div>
<div class="step l4 abs fragment" style="left:360px; top:300px;"><small>platform value · hardware engineer</small>DELAY_T1H = 700 ns × CPU clock / 10⁹<br>(number of NOPs for a high bit)</div>
</div>
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

### A component

<div class="stage">
<div class="tile abs" style="left:350px; top:180px;" data-id="comp">light_controller</div>
</div>

Note:

One tile from the stack. Next click: open it.

---

<!-- .slide: data-auto-animate data-auto-animate-id="comp" -->

### A component

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:96px; width:880px;">
<div class="comp abs" style="left:130px; top:40px;" data-id="comp">
<b>light_controller</b> &nbsp; <span class="tag">scope: SPL</span><br>
<span class="k">code</span> src/light_controller.c, .h<br>
<span class="k">tests</span> test/test_light_controller.cc<br>
<span class="k">docs</span> doc/index.md<br>
<span class="k">features</span> KConfig
</div>
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

### Who can read your model?

<div class="stage">
<!-- Centres the content in the stage. -->
<div class="abs" style="left:0; top:26px; width:880px;">
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

### One command per cell

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
