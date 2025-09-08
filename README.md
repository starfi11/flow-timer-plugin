# flow-timer-plugin

**flow-timer-plugin** is a timer plugin that lets you control multiple countdown timers using commands through Flow Launcher.
It supports starting, canceling, and resetting timers, and provides notifications when a timer finishes.

---

## 🕹️ How to Use

To start a timer, use the plugin keyword `timer` followed by the `start` command:

```
timer start <name> <time>
```

* `<name>`: the label of your timer (e.g., `tea`, `study`, `focus`)
* `<time>`: the countdown duration, supporting any combination of `h` (hours), `m` (minutes), and `s` (seconds) in any order

Example:

![Start Example 1](https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081606754.png)

The `start` keyword is optional. You can omit it and simply write:

![Start Example 2](https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081607135.png)

---

## ⏲️ Timer Behavior

Once started, a floating timer window will appear on the right edge of your screen.

When the countdown reaches zero:

* A beeping sound will play for **3 seconds**
* The timer window will enter a **flashing gradient state** for **5 seconds**

<div style="overflow: auto;">
  <img src="https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081608520.png" alt="Static timer image" style="width: 40%; float: left;">
  <img src="https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081612185.gif" alt="Flashing animation" style="width: 40%; float: right;">
</div>

After this alert phase, the timer enters a **negative counting mode** (it continues counting below zero) to show overtime duration, and will stay on screen until manually closed.

---

## 🛑 Cancel a Timer

Use the `cancel` command followed by the timer’s label to stop a specific timer:

```
timer cancel <name>
```

Example:

![Cancel Example](https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081615695.png)

---

## ♻️ Reset a Timer

Use the `reset` command followed by the timer’s label to restart it from its original countdown:

```
timer reset <name>
```

Example:

![Reset Example](https://luweiphoto.oss-cn-wuhan-lr.aliyuncs.com/202509081616465.png)

---

Let me know if you want to add installation instructions, plugin settings, known issues, or advanced tips!
