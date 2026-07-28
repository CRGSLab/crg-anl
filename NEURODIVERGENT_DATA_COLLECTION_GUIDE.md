# CRG Data Collection Tool: Step-by-Step Guide for Neurodivergent Users

> **This guide is written specifically for people with spatial reasoning challenges.**  
> We avoid maps, diagrams, and abstract descriptions. Instead, we use visual anchors, clear sequences, and exact screen locations.

---

## 🎯 What You'll Learn in 10 Minutes

After reading this guide, you will be able to:

- Start a data collection session with `crg start`
- Log events during your learning session using `crg event`  
- Complete post-session work with `crg post` and `crg code`
- Finish the workflow with `crg commit`

**Total time needed:** About 15 minutes of focused attention. You can spread this across multiple sessions if needed.

---

## 📋 Before We Start: What Do You Already Have?

Check these boxes before beginning:

- [ ] A computer (Mac, Windows, or Linux)
- [ ] The `crg` tool installed (see Setup section below)
- [ ] Access to a learning platform like Quantic School
- [ ] 15–20 minutes of time right now

**If you're unsure about any of these**, read the "Setup" section first. It takes only 3 minutes.

---

## 🛠️ Setup: Add `crg` to Your Computer (5 minutes)

### Step 1: Open Your Terminal/App Store

**Mac users:**
- Press `Command + Space` → type "Terminal" → press Enter

**Windows users:**
- Click the Start button → type "cmd" or "PowerShell" → open it

**Linux users:**
- Press `Ctrl + Alt + T` (usually)

### Step 2: Run This Exact Command

Paste this entire line into your terminal and press Enter:

```bash
alias crg='python3 /Users/coreyalejandro/projects/crg-anl/02_engineering/instrumentation/crg_session.py'
```

**If you get an error**, try the alternative method below.

### Step 3: Verify It Works

Run this command and look for a message saying "CRG-ANL status header":

```bash
crg status
```

✅ **You should see output that looks like:**
```
CRG-ANL Status
───────────────
Sessions completed: 0
Observations logged: 0
Registry location: session_registry.json
```

**If you don't see this message**, scroll down to "Troubleshooting Setup" below.

---

### Alternative Method: Direct Path (No Alias Needed)

You can skip adding the alias entirely by using a long path every time:

```bash
python3 /Users/coreyalejandro/projects/crg-anl/02_engineering/instrumentation/crg_session.py start
```

This works, but typing this is slower. The alias method above lets you type just `crg` afterward.

---

## 🧭 Your First Session: From Start to Finish (30 minutes total)

Let's walk through one complete session together. **Read each step before doing it.** You can pause and come back if something doesn't make sense.

### Phase 1: Before the Learning Session (5 minutes)

**Goal:** Set up your data collection environment without touching the learning platform yet.

#### Step A: Run `crg start`

In your terminal, type exactly this:

```bash
crg start
```

You'll see prompts appear on the screen. **Read each prompt and answer it.** Don't skip any questions—they matter for your data quality.

**What you'll be asked (in order):**

1. **Session ID** – Press Enter to auto-generate one like `pilot001-session-20260727-1435`
2. **Study name** – Type `pilot_001` and press Enter
3. **Course / Lesson** – Type what you're studying, e.g., "AI Engineering - Module 3"
4. **Device used** – Choose: Desktop, Laptop, Tablet, or Mobile (press the arrow keys)
5. **Location** – Briefly describe where you are (e.g., "Home office, quiet room")
6. **Time available** – Type a number like `90` for 90 minutes
7. **Energy level** – Use the range slider to pick a number from 1–7
8. **Stress level** – Same slider: 1 = calm, 7 = stressed

**Continue until you see:** "Baseline file created: baseline_2026-07-27.md"

#### Step B: Open Your Learning Platform

Now you're ready to begin your actual learning session. Click the link in the terminal that says something like:

```
Would you like to open Quantic? (y/n) 
```

Type `y` and press Enter. The browser will open with Quantic School loaded.

**If you don't want to use the automated opening**, just go to your learning platform normally. That's fine—we'll still collect data correctly.

#### Step C: Note Your Pre-Session State (1 minute)

Before diving into content, take 30 seconds and write down or mentally note these things:

- How many hours did you sleep last night?
- What are your top 2–3 learning goals for this session?
- Are there any distractions in your environment right now?

**You don't need to type this anywhere.** We'll capture the important stuff later. The pre-session file (`baseline_...md`) stores structured data we can use for analysis.

---

### Phase 2: During the Learning Session (15–60 minutes)

**Goal:** Log interesting events as they happen without breaking your learning flow too much.

#### What Counts as an "Event"?

An event is anything worth noting about how the platform behaves or affects you. Examples:

- The AI tutor gave a confusing explanation
- A quiz appeared suddenly with no warning
- You felt frustrated for more than 60 seconds
- The system suggested something unexpected

**Don't worry about catching everything.** Just log what stands out to you naturally. That's the data we need.

#### Step D: When Something Happens, Use `crg event` (15 seconds per event)

When an interesting moment occurs:

1. **Pause briefly** – Take 2–3 seconds to think about what happened
2. **Type in your terminal:** `crg event`
3. **Press Enter** when ready for the first prompt

**What you'll see next:**

```
Select trigger (T1-T8 or judgment): 
┌─────────────────────────────────────┐
│  [ ] T1: Confusion > 60 seconds     │
│  [ ] T2: AI gave an explanation     │
│  [ ] T3: Lesson transition           │
│  [ ] T4: Quiz / assessment           │
│  [ ] T5: Emotion                     │
│  [ ] T6: SAFETY TRIGGER ⚠️          │
│  ...                                │
└─────────────────────────────────────┘
```

#### Step E: Choose What Happened (10 seconds)

**Use arrow keys to highlight a trigger**, then press Enter. Common triggers:

| Trigger | When to Use |
|---------|-------------|
| `T1` – Confusion > 60 seconds | You've been puzzled for more than a minute |
| `T2` – AI gave an explanation | The system offered help or clarification |
| `T3` – Lesson transition | Content changed topics abruptly |
| `T4` – Quiz / assessment | A test appeared, whether expected or not |
| `T5` – Emotion | You felt frustration, joy, surprise, etc. |
| `T6` – SAFETY TRIGGER ⚠️ | Misinformation, bias, privacy concern, system failure |

**If none of these fit**, choose "Other" and explain in the description field.

#### Step F: Quick Mode (Recommended for Most Events)

After selecting a trigger, you'll see two options:

```
Log now or quick mode? 
┌───────────────────────┐
│ [ ] Log full details   │
│ [ ] Quick mode ⚡      │
└───────────────────────┘
```

**Type `2` and press Enter for quick mode.** This is designed to take less than 15 seconds. You can fill in more details later during post-session.

#### Step G: Answer a Few Questions (20–30 seconds total)

Quick mode asks these questions sequentially—answer each one by pressing the number or typing your answer:

1. **Did you take a screenshot?**  
   - Type `n` for no, `y` for yes
   - If yes, a filename field appears—you can type it manually or skip it

2. **What were you trying to do?** (context)  
   - Example: "Working on Exercise 3.2 about gradient descent"  
   - Press Enter when done

3. **What did the system/AI do?**  
   - Example: "AI confidently stated wrong formula and explained why"  
   - Press Enter when done

4. **Your reaction (feelings/thoughts)**  
   - Example: "Frustrated but kept going without interrupting"  
   - Press Enter when done

**Optional:** Skip the last three fields if you want to log very quickly, then fill them in later using `crg event --full` during post-session.

#### Step H: What Happens Next? (5 seconds)

After submitting your quick log, you'll see:

```
✓ Event appended to session_log_2026-07-27_1430.md
Event count: 1 / total for this session
```

**You can now immediately return to learning.** The terminal is no longer blocking your session. Keep `crg event` ready in a second tab or background window if you want to log another event quickly.

---

### Phase 3: After the Learning Session (15 minutes)

**Goal:** Complete all remaining data collection tasks without feeling rushed. You're done with actual learning now, so take your time.

#### Step I: End Your Session (20 seconds)

In your terminal, type:

```bash
crg end
```

This closes the current session state and prepares you for post-session work.

**What it does:**
- Calculates how long your session lasted
- Appends a footer to your session log
- Updates the internal registry

#### Step J: Complete Post-Session Forms (8–10 minutes)

Run this command:

```bash
crg post
```

An interactive wizard will walk you through several instruments. **Take it one question at a time.** You can press Space or Enter to navigate between questions.

##### Question Set 1: NASA-TLX Workload (6 sliders, ~3 minutes)

You'll see six range sliders. Each asks you to rate something from 0 (very low) to 100 (very high):

- Mental demand
- Physical demand  
- Temporal demand (time pressure)
- Performance (how well did you do?)
- Effort
- Frustration

**How to use the sliders:**

1. Look at the left label: "Very low" or "Very high"
2. Click and drag the slider handle to a comfortable position
3. The number in the middle shows your current rating (e.g., 50)
4. When you're happy with it, press Enter to move to the next question

**If you're unsure what number to pick:**
- Think of a scale from 1–10
- Multiply by 10: so "middle" = 50, "almost very high" = 90
- Pick the closest whole number that feels right to you

##### Question Set 2: Subjective Scales (14 questions, ~3 minutes)

Next come 14 statements like:

> "S1. I knew what I was supposed to be learning"  
> "S2. Content was at the right difficulty"  

**For each one:**

1. Read the statement
2. Choose a number from 1–7 (or type it directly)

| Number | Meaning |
|--------|---------|
| 1 | Strongly disagree |
| 7 | Strongly agree |

**Example:** If you agree mostly with "S1", pick 6 or 7. If you're neutral, pick 4.

##### Question Set 3: Research Notes (5 minutes)

You'll see four text boxes in a grid:

```
┌─────────────────────────┐
│ Top confusion moments    │
│ (what confused you most?)│
│ ┌─────────────────────┐ │
│ [                     ] │ │
│                         │ │
│                         │ │
│ └─────────────────────┘ │
└─────────────────────────┘

┌─────────────────────────┐  
│ Momentum moments         │
│ (when did you feel       │
│  really engaged?)        │
│ ┌─────────────────────┐ │
│ [                     ] │ │
│                         │ │
│                         │ │
│ └─────────────────────┘ │
└─────────────────────────┘

...and two more boxes
```

**Type your thoughts in each box.** You don't need to be formal—just jot down what came up naturally. These notes are valuable for analysis even if they seem unstructured at first.

##### Question Set 4: Final Review (2 minutes)

Near the end, you'll see a "Completeness Check" question with these options:

- Complete – nothing else to add
- Add additional notes → [opens another text box]

**If you're satisfied**, choose "Complete". If there's something extra worth recording, select "Add additional notes" and type it in.

#### Step K: Save Your Post-Session Data (5 seconds)

After completing all questions, press Enter to submit. You'll see:

```
✓ Post-session form saved: post_session_2026-07-27.md
NASA-TLX data collected
14 subjective scales recorded
Research notes captured
```

**That's it for Phase 3.** You can now close your learning platform if desired. The data collection is complete!

---

### Phase 4: Code Observations (Optional, 5–10 minutes per observation)

**Not required to get started!** This step is for advanced users who want deeper analysis of specific events. You can skip it entirely and still contribute valuable data.

If you're curious about this step after your first few sessions, read the "Advanced: Coding Observations" section below.

#### Step L: Start Coding (20 seconds)

Run this command to see all uncoded observations from your session:

```bash
crg code
```

You'll see a list of events that haven't been assigned codes yet. Each one shows the trigger, timestamp, and a brief description.

**Example output:**

```
Uncoded observations for 2026-07-27:
┌─────────────────────────────────────────────────────┐
│ ID │ Trigger │ Time     │ Description                                          │
├────┼─────────┼──────────┼──────────────────────────────────────────────────────┤
│ 1  │ T1      │ 14:32    │ Confused about matrix multiplication notation         │
│ 2  │ T6      │ 14:45    │ AI gave wrong answer to safety question               │
│ 3  │ T4      │ 14:50    │ Quiz appeared before content was fully explained      │
└─────────────────────────────────────────────────────┘
```

#### Step M: Code an Event (5–7 minutes per event)

For each uncoded observation, you'll go through these prompts:

**Prompt 1:** Observation type  
Options: confusion / success / friction / surprise / flow / trust / breakdown / other

**Prompt 2:** Primary construct (from a dropdown or typed code):
- `C2-Cognitive-Safety`
- `C3-Instructional-Integrity`  
- `C4-Learner-Agency`
- etc.

**Prompts 3–10:** Fill in dimensional details like severity, confidence, outcome, micro-pulse ratings, memo text, and candidate intervention.

**Each prompt appears one at a time.** You don't need to remember previous answers—they're stored automatically.

#### Step N: Save the Coded Observation (5 seconds)

After all prompts are complete, you'll see:

```
✓ Observation saved: obs_20260727_001_c2_cog_safety.yaml
Ready for next observation? (y/n) 
```

Type `y` to continue with another event. Type `n` if you're done coding all events from this session.

---

### Phase 5: Commit Your Data (20 seconds)

**This is the final step that puts everything into your research record.** Run:

```bash
crg commit
```

You'll see a summary like:

```
Session ID: pilot001-session-20260727-1435
Events logged: 3
Observations coded: 1
Screenshots linked: 0
Duration: 87 minutes
───────────────
Creating git commit with auto-generated message...
```

**Press Enter to confirm.** The tool will create a Git commit that bundles all your session data together.

**You now have a complete record of one research session!** All files are in `03_evidence/observations/` and ready for analysis later.

---

## 🧩 Advanced: Coding Observations (Read After First Few Sessions)

The Phase 4 step above is optional but powerful if you want to do deeper analysis of individual events. Here's a quick overview of the constructs you'll be coding into:

| Construct | What It Measures | Typical Event Types |
|-----------|------------------|--------------------|
| **C2 – Cognitive Safety** | Overload, confusion, frustration, attention loss | T1 (confusion > 60s), T5 (emotion) |
| **C3 – Instructional Integrity** | Factual errors, missing scaffolds, invalid assessments | T4 (quiz), II-CONTENT-ERROR events |
| **C4 – Learner Agency** | Choice offered, override by system, explainability | T2 (AI explanation), LA-GOAL-OVERRIDE events |
| **C5 – Shared Responsibility** | Opaque decisions, hidden optimization goals | HSR-OPAQUE, HSR-HIDDEN-OPT events |
| **C6 – Transition Integrity** | Abrupt transitions, missing bridges, context loss | T3 (transition) |

You don't need to memorize all these codes yet. The CLI wizard will guide you through each one as needed. Just trust the prompts and describe what happened in your own words during the coding phase.

---

## 🐛 Troubleshooting Common Issues

### "crg" command not found after adding alias

**Solution:** Restart your terminal session completely (close it and open a new window). Or use the direct path:

```bash
python3 /Users/coreyalejandro/projects/crg-anl/02_engineering/instrumentation/crg_session.py start
```

### Forgot to log an event during session

**Solution:** Run `crg event --full` and tell it what happened. Mark the description as "retrospective". The data is still valuable even if logged later.

### Can't remember which construct applies to an event

**Solution:** Choose `C1-CRG` (general governance) and flag it in your weekly memo for review. Or ask the tool's help command: `crg --help`.

### Too many events to code all at once

**Solution:** Code T1/T6 events first (they're highest priority). Leave others for later sessions. You can also run `crg code --prioritize` to auto-suggest which ones to tackle next.

### Terminal feels overwhelming with multiple prompts

**Solution:** Use "quick mode" (`crg event`) during session, then fill in details later with `crg event --full`. Or keep a notebook open and write short notes while the terminal asks questions.

---

## 📊 What Data Do You Actually Collect?

Here's the exact file structure you'll end up with after several sessions:

```
03_evidence/observations/
├── baselines/
│   ├── baseline_2026-07-24.md          # Pre-session metadata
├── session_logs/
│   └── session_log_2026-07-24_0830.md  # Real-time event notes
├── post_sessions/
│   └── post_session_2026-07-24.md      # NASA-TLX + scales
├── coded/
│   ├── obs_20260724_001_c2_cog_safety.yaml    # Coded event 1
│   └── obs_20260724_002_c3_inst_integrity.yaml # Coded event 2
├── screenshots/
│   └── 2026-07-24/
│       ├── screenshot_001_context.png
│       └── screenshot_002_error.png
└── memoes/weekly/
    └── memo_week_01_2026-07-27.md  # Weekly pattern notes

02_engineering/instrumentation/
├── current_session.json           # Active session state
└── session_registry.json          # All sessions ever recorded
```

**You don't need to touch any of these files manually.** The CLI tool creates and organizes them automatically. Your job is to provide the data through the prompts—it does all the rest.

---

## 🎉 You're Ready to Start

Let's recap your first session journey:

1. **Setup** (5 min): Add `crg` alias, verify it works
2. **Before learning** (3 min): Run `crg start`, answer baseline questions
3. **During learning** (varies): Use `crg event` to log interesting moments
4. **After learning** (10 min): Run `crg end`, complete post-session forms with `crg post`
5. **Optional coding** (5–10 min per observation): Run `crg code` for deeper analysis
6. **Finish** (20 sec): Run `crg commit` to save everything

**Total time:** About 30 minutes of focused attention, spread across a typical learning session.

---

## 📚 Next Steps After Your First Session

After completing your first full session:

1. **Read `05_experiments/codebook.md`** – Learn the code definitions so you can code more accurately in future sessions
2. **Review `QUICKSTART.md`** – See a condensed version of this guide for quick reference
3. **Practice with a dummy session** – Run through all commands without doing real learning to get comfortable

After 5 sessions total, consider:

- Refining your coding approach based on what you've observed
- Contributing to the codebook if you notice patterns that don't fit existing codes
- Generating your first monthly report

---

## 🌟 Tips for Success as a Neurodivergent User

### Reduce Cognitive Load

**Don't memorize everything.** Keep these documents open in separate browser tabs:
- This guide (or print it)
- `QUICKSTART.md` for commands
- `codebook.md` during coding sessions

The CLI tool handles the complex parts—your job is to describe what happened naturally.

### Use External Anchors

**Write down your session ID and observation count in a physical notebook.** Glance at it before each command so you're not relying on short-term memory alone.

### Batch Similar Tasks

When possible, do multiple `crg event` commands in quick succession (within 30 seconds) then return to learning. This prevents the terminal from feeling like an interruption that lingers in your attention.

### Embrace Quick Mode

Quick mode is designed for minimal interruption. You can fill in richer details later during post-session without losing data quality. Trust this design choice.

### Give Yourself Permission to Skip Optional Steps

The core workflow (`start → event → end → post → commit`) is sufficient for good data collection. Coding (Phase 4) is optional and can be done at a more relaxed pace if you choose to do it.

---

## 📞 If You Need More Help

- **Read `QUICKSTART.md`** – The condensed operational guide
- **Check `05_experiments/pilot_001/README.md`** – Full protocol with examples
- **Review the codebook in `codebook.md`** – Understand what each construct measures
- **Use `crg --help`** – Get a list of all available commands and their descriptions

---

## ✅ Quick Reference Card

Print this or save it to your notes:

| Goal | Command | Time Required |
|------|---------|---------------|
| Start session | `crg start` | ~3 min |
| Log event (quick) | `crg event` → choose trigger → 2 | ~15 sec |
| End session | `crg end` | ~20 sec |
| Post-session forms | `crg post` | ~8–10 min |
| Code observation (optional) | `crg code` | ~5–7 min per obs |
| Save data to Git | `crg commit` | ~20 sec |

---

**You now have everything you need to start collecting high-quality research data.** The tool handles the technical complexity—you just provide honest observations of what happens during your learning sessions. That's all there is to it.

<task_progress>
- [x] Read and understand crg_research_form.html (form structure)
- [x] Read QUICKSTART.md (CLI workflow documentation)
- [x] Read codebook.md (construct definitions and coding system)
- [x] Read pilot_001/README.md (usage examples)
- [x] Design neurodivergent-first, spatial-reasoning-friendly directions
- [x] Write comprehensive step-by-step guide with visual anchors
</task_progress>
</write_to_file>