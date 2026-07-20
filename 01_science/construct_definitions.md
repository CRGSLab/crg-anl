# Construct Definitions

**Artifact:** Construct Definitions  
**Version:** 0.1.0  
**Status:** Foundation complete — subject to refinement through pilot studies  
**Canonical:** Yes — governs all downstream research terminology and measurement  

---

## Overview

This document defines the canonical constructs of the CRG-ANL Research Program.
Each construct includes: a formal definition, theoretical motivation, relationships to other constructs, example observations from AI-native educational environments, and future benchmark dimensions that will be developed as the research program matures.

Constructs are organized from the most abstract (Constitutional Runtime Governance) to the most specific (Researcher-as-Subject methodology).

---

## C1: Constitutional Runtime Governance

### Definition

A governance model in which principled behavioral constraints — a "constitution" — are applied to AI instructional agents dynamically during runtime, governing every instructional action (content generation, scaffolding, assessment, feedback, navigation, and transitions) in real time, with observable enforcement, violation detection, and intervention mechanisms.

Constitutional Runtime Governance is distinguished from:
- **Static safety filters** (applied pre-deployment, not responsive to runtime context)
- **Post-hoc audits** (conducted after harm, not preventive)
- **Technical guardrails** (rule-based output filtering without principled grounding)
- **Human-in-the-loop oversight** (reactive human review, not systematic automated governance)

### Theoretical Motivation

Traditional AI governance operates at two timescales: design-time (safety training, alignment research) and audit-time (evaluation benchmarks, red-teaming).
Neither timescale addresses the instructional moment — the specific interaction between learner and AI system during which cognitive harm or instructional integrity failure can occur.

Constitutional Runtime Governance introduces a third timescale: **runtime governance**, operating continuously during every instructional interaction.
This is necessary because:

- Instructional context is too variable to address fully at design time
- Post-hoc audits cannot prevent harm to the current learner
- The instructional arc (content → scaffolding → assessment → feedback → transition) requires governance at each stage
- Learners need observable evidence that governance is active (the Learner Cockpit)

The theoretical foundation draws on:
- **Constitutional AI** (Bai et al., Anthropic) — the idea that AI systems can be governed by principles rather than just training data
- **Dynamic safety monitoring** (AI safety literature) — real-time detection of hazardous outputs
- **Instructional design theory** (Merrill, Gagné, Sweller) — systematic principles for effective learning
- **Cognitive load theory** (Sweller, Paas, van Merriënboer) — management of mental demand during learning

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C2 Cognitive Safety | **Protects** | CRG is the governance mechanism; Cognitive Safety is the outcome it protects |
| C3 Instructional Integrity | **Enforces** | CRG enforces Instructional Integrity through runtime constraints |
| C4 Learner Agency | **Preserves** | CRG includes constraints that prevent agency erosion |
| C5 Human–AI Shared Responsibility | **Governs** | CRG governs the distribution of responsibility |
| C6 Transition Integrity | **Maintains** | CRG applies specific constraints during transitions |
| C7 Runtime Intervention | **Triggers** | CRG triggers interventions when constraints are violated |
| C8 Learner Cockpit | **Displays** | CRG state is displayed through the Learner Cockpit |
| C9 Persistent Runtime Governance Window | **Operates within** | CRG operates continuously within the PRGW |
| C10 Governance Benchmark | **Evaluated by** | CRG effectiveness is measured by Governance Benchmarks |
| C11 Researcher-as-Subject | **Studied through** | CRG is empirically investigated through researcher-as-subject methodology |

### Example Observations

- **Positive:** The AI tutoring system states, "I am not certain about this answer. Here is what I know, and here is what you should verify independently." This demonstrates epistemic humility enforced by runtime governance.
- **Negative:** The AI system generates a plausible but incorrect explanation of backpropagation without any uncertainty marker or source attribution. This indicates a CRG failure — specifically, an Instructional Integrity violation that runtime governance failed to prevent.
- **Positive:** When the learner makes three consecutive errors on a concept, the system automatically reduces difficulty and provides a worked example, while displaying "Adapted: difficulty reduced" in the Learner Cockpit. This demonstrates adaptive scaffolding governed by CRG with observable enforcement.
- **Negative:** During a transition from a video lesson to an interactive quiz, the AI changes topics without warning, leaving the learner confused about the connection. This is a Transition Integrity failure — a gap in the Persistent Runtime Governance Window.

### Future Benchmark Dimensions

- Constitution coverage: What percentage of instructional actions are governed?
- Violation detection latency: How quickly are violations detected?
- Intervention effectiveness: Do interventions restore safe learning conditions?
- Learner comprehension of governance: Do learners understand what is being governed and why?
- Constitution adaptability: Can the constitution be updated based on evidence?

---

## C2: Cognitive Safety

### Definition

The protection of a learner's cognitive resources — attention, working memory, executive function, metacognitive capacity, and emotional equilibrium — from harm caused by AI-mediated instructional design.

Cognitive Safety is not merely the absence of cognitive load.
Appropriate cognitive challenge (germane load) is essential for learning.
Cognitive Safety protects against:
- **Cognitive overload** — extraneous load exceeding processing capacity
- **Attention fragmentation** — design elements that disrupt sustained attention
- **Metacognitive disruption** — AI actions that impair the learner's ability to monitor their own understanding
- **Emotional distress** — anxiety, frustration, or demotivation caused by instructional design
- **Confusion without resolution** — sustained confusion that the system fails to detect or address

Cognitive Safety is distinct from:
- **Cognitive load** (a measurement construct, not a safety framework)
- **Usability** (concerned with efficiency and satisfaction, not cognitive harm)
- **Accessibility** (concerned with inclusive design for disabilities, though overlapping)

### Theoretical Motivation

Cognitive Safety emerges from the intersection of three research traditions:

1. **Cognitive Load Theory** (Sweller, 1988; Paas & Sweller, 2012) establishes that working memory is limited and that instructional design can either support or overwhelm it.
However, CLT focuses on optimization, not on harm prevention.
Cognitive Safety extends CLT by asking: what instructional design choices actively damage cognitive resources?

2. **AI Safety** (Russell, Amodei, Bengio) focuses on preventing catastrophic outcomes from AI systems.
Cognitive Safety operationalizes AI safety for the educational domain, where "catastrophic" may mean a learner developing a fundamental misconception, losing confidence, or abandoning a learning path.

3. **Emotional Design** (Norman, 2004; Picard, 1997) recognizes that cognitive and emotional states are interdependent.
Cognitive Safety explicitly includes emotional equilibrium as a protected cognitive resource.

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Protected by** | CRG is the primary mechanism for ensuring Cognitive Safety |
| C3 Instructional Integrity | **Depends on** | Instructional Integrity failures (incorrect content, poor scaffolding) are major sources of cognitive harm |
| C4 Learner Agency | **Enabled by** | Cognitive Safety is a precondition for meaningful Learner Agency — a cognitively overwhelmed learner cannot exercise agency |
| C5 Human–AI Shared Responsibility | **Requires** | Safe distribution of cognitive labor requires that neither party is overloaded |
| C6 Transition Integrity | **Threatened by** | Transitions are high-risk moments for Cognitive Safety failures |
| C8 Learner Cockpit | **Monitored via** | The Learner Cockpit displays real-time Cognitive Safety indicators |

### Example Observations

- **Cognitive overload:** The AI presents five new concepts simultaneously in a single interaction, each requiring working memory resources.
The learner's NASA-TLX mental demand score spikes to 85/100.
The system fails to detect the overload and continues presenting new material.
- **Attention fragmentation:** The mobile interface interrupts the lesson with three notifications, a badge animation, and a prompt to share progress on social media during a cognitively demanding explanation.
- **Metacognitive disruption:** The AI provides a complete worked solution before the learner has attempted the problem, eliminating the opportunity for self-assessment and strategy selection.
The learner reports feeling "like the AI is doing my thinking for me."
- **Emotional distress:** After two incorrect answers, the AI responds with "That's not right. Try again." (no explanation, no scaffolding, no affective acknowledgment).
The learner's frustration score increases from 2/7 to 6/7, and they consider abandoning the session.

### Future Benchmark Dimensions

- Cognitive overload detection rate: What percentage of overload episodes does the system detect?
- Overload recovery time: How long until cognitive load returns to safe levels after an overload event?
- Attention fragmentation index: How many attention-disrupting events occur per learning hour?
- Metacognitive support frequency: How often does the system prompt self-assessment or strategy reflection?
- Emotional safety score: Composite measure of frustration, anxiety, and demotivation indicators

---

## C3: Instructional Integrity

### Definition

The property of an AI-native educational system whereby its instructional actions — content generation, scaffolding, assessment, feedback, navigation, and transitions — are accurate, coherent, consistent, and aligned with stated learning objectives.

Instructional Integrity encompasses six sub-dimensions:

| Dimension | Definition |
|-----------|-----------|
| **Assessment Integrity** | Assessments accurately measure the learning objectives they claim to measure, at an appropriate difficulty level, with valid distractors and scoring |
| **Scaffolding Integrity** | Scaffolding content is factually correct, pedagogically complete, conceptually coherent, and appropriately paced |
| **Navigation Integrity** | The system guides learners through content in a coherent sequence that supports progressive knowledge construction |
| **Transition Integrity** | Transitions between instructional states preserve cognitive continuity, epistemic orientation, and learner agency (see C6) |
| **Feedback Integrity** | Feedback is accurate, specific, actionable, and aligned with the learner's actual performance and the learning objectives |
| **Accessibility Integrity** | Instructional content is accessible to learners with diverse cognitive profiles, sensory abilities, and backgrounds |

Instructional Integrity is distinct from:
- **Factual accuracy** (a necessary but insufficient component — integrity requires pedagogical and contextual appropriateness)
- **Content quality** (broader than integrity — includes engagement, relevance, currency)
- **System reliability** (technical uptime, not instructional quality)

### Theoretical Motivation

Generative AI systems are inherently prone to instructional integrity failures because:

- They generate novel content rather than retrieving verified content
- They lack epistemic self-awareness — they cannot reliably distinguish knowledge from inference from fabrication
- They are optimized for plausibility, not pedagogical soundness
- They have no inherent understanding of learning objectives, prerequisite structures, or conceptual dependencies
- They can be inconsistent across similar queries, producing contradictory explanations

These failures are not merely technical errors.
They are **pedagogical harms**:

- An incorrect explanation of a concept can create a misconception that persists and compounds
- An assessment that measures the wrong construct provides invalid feedback to both learner and system
- Inconsistent feedback erodes trust and creates confusion about what constitutes correct understanding

Instructional Integrity draws on:
- **Validity theory** (Messick, Kane) — the alignment between assessment and construct
- **Pedagogical content knowledge** (Shulman) — the intersection of subject matter and instructional expertise
- **Error analysis in intelligent tutoring systems** (VanLehn, Koedinger)

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Enforced by** | CRG applies constraints that prevent Instructional Integrity failures |
| C2 Cognitive Safety | **Threatens** | Instructional Integrity failures are a primary source of cognitive harm |
| C4 Learner Agency | **Supports** | High Instructional Integrity enables informed agency; low integrity forces dependency |
| C5 Human–AI Shared Responsibility | **Requires** | Shared responsibility requires that the AI's instructional contributions are reliable |
| C6 Transition Integrity | **Sub-dimension of** | Transition Integrity is one of the six dimensions of Instructional Integrity |

### Example Observations

- **Scaffolding integrity failure:** The AI explains gradient descent using terminology (" Jacobian matrix") that has not been introduced in the curriculum, creating confusion without the learner having a reference point.
- **Assessment integrity failure:** A quiz question asks about a concept not covered in the preceding lesson, producing a false negative (the learner knows the taught material but not the untaught material).
- **Feedback integrity failure:** The AI marks a partially correct answer as completely wrong without identifying which components were correct, missing an opportunity for targeted remediation.
- **Navigation integrity failure:** The curriculum jumps from basic linear algebra to eigenvalue decomposition without intermediate steps, breaking the conceptual progression.

### Future Benchmark Dimensions

- Hallucination rate by instructional dimension: What percentage of generated content contains factual errors?
- Consistency score: How consistent are explanations of the same concept across different sessions?
- Assessment validity index: Correlation between assessment scores and independent measures of the target construct
- Feedback specificity: Average number of specific, actionable elements per feedback instance

---

## C4: Learner Agency

### Definition

The capacity of a learner to set, pursue, and revise their own learning goals, strategies, and evaluative standards within an AI-native educational environment.

Learner Agency has four operational components:

| Component | Description |
|-----------|-------------|
| **Goal-setting** | The learner can define what they want to learn, why, and to what depth |
| **Strategy selection** | The learner can choose how to approach learning (pace, sequence, modality, depth) |
| **Self-assessment** | The learner can evaluate their own understanding against their own or external standards |
| **Revision** | The learner can change goals, strategies, or standards based on self-assessment |

Learner Agency is distinct from:
- **System adaptivity** (the system adjusting to the learner — agency is the learner adjusting the system or their own approach)
- **User control** (interface-level control over settings — agency is deeper, involving epistemic and strategic autonomy)
- **Motivation** (agency can support motivation, but they are distinct constructs)

### Theoretical Motivation

Adaptive AI tutoring systems pose a unique threat to Learner Agency.
When an AI system makes decisions about what content to present, at what difficulty, in what sequence, and with what feedback, it can systematically displace the learner's own goal-setting, strategy selection, and self-assessment processes.

This is not merely a usability concern.
It is an **epistemic concern**:

- A learner who never chooses what to learn may not develop the metacognitive skills to identify their own knowledge gaps
- A learner who never evaluates their own understanding may not develop self-regulated learning capacity
- A learner who always follows AI-recommended paths may not discover alternative approaches or connections

Learner Agency draws on:
- **Self-Determination Theory** (Deci & Ryan) — autonomy as a basic psychological need
- **Self-Regulated Learning** (Zimmerman, Pintrich) — the learner's active management of their own learning
- **Epistemic Agency** (Chinn, Rinehart, Buckland) — the capacity to engage in productive epistemic practices

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Preserved by** | CRG includes constraints that prevent agency erosion |
| C2 Cognitive Safety | **Depends on** | Cognitive Safety is a precondition for Agency — overwhelmed learners cannot exercise agency |
| C3 Instructional Integrity | **Requires** | Learners need accurate information to make informed agency decisions |
| C5 Human–AI Shared Responsibility | **Core of** | Agency defines what the human retains in the shared responsibility distribution |
| C8 Learner Cockpit | **Enabled by** | The Learner Cockpit provides the transparency needed for informed agency |

### Example Observations

- **Agency present:** The learner can see a curriculum map, select which topic to study next, set their own session duration, and override the AI's difficulty recommendation.
The AI explains why it recommended a particular path but defers to the learner's choice.
- **Agency eroded:** The AI automatically advances to the next lesson when the learner achieves 80% on the quiz, without asking if the learner wants to review, explore related topics, or pause.
The learner feels "pushed along a conveyor belt."
- **Agency present:** The AI asks, "Would you like me to explain this differently, provide a worked example, or let you try another problem on your own?" — offering strategic choice.
- **Agency eroded:** The AI provides complete solutions to all practice problems, never offering the learner the opportunity to struggle, fail, and learn from error.

### Future Benchmark Dimensions

- Goal-setting support: Does the system prompt and record learner-defined goals?
- Strategy choice availability: How many distinct learning strategies does the system offer?
- Override frequency: How often do learners override AI recommendations, and what happens when they do?
- Self-assessment prompts: How frequently does the system prompt metacognitive reflection?
- Agency perception: Learner self-report of perceived control and choice

---

## C5: Human–AI Shared Responsibility

### Definition

The negotiated distribution of cognitive, epistemic, and instructional labor between human learner and AI system, characterized by appropriate delegation, oversight, and mutual accountability.

Human–AI Shared Responsibility involves three labor domains:

| Domain | Human Responsibility | AI Responsibility | Shared |
|--------|---------------------|-------------------|--------|
| **Cognitive** | Sustaining attention, effort, metacognitive monitoring | Reducing extraneous load, providing scaffolding | Managing total cognitive demand |
| **Epistemic** | Evaluating claims, seeking verification, maintaining skepticism | Providing accurate information, expressing uncertainty | Establishing what counts as knowledge |
| **Instructional** | Setting goals, selecting strategies, self-assessing | Generating content, adapting difficulty, providing feedback | Designing the learning experience |

The distribution is **negotiated** — it can change based on context, learner preference, and instructional phase.
It is not fixed.

### Theoretical Motivation

The default distribution of responsibility in adaptive AI tutoring systems is heavily skewed toward the AI.
The AI decides what to teach, how to teach it, when to assess, how to adapt, and what feedback to give.
The learner's role is reduced to responding to AI-initiated actions.

This skewed distribution is problematic because:

- It contradicts established learning science showing that active, self-directed learning produces deeper understanding
- It creates dependency — learners may struggle when AI support is unavailable
- It obscures the AI's limitations — learners may not recognize when the AI is wrong or uncertain
- It prevents the development of self-regulated learning skills

Human–AI Shared Responsibility proposes an alternative: a **dynamic, transparent, negotiable** distribution in which:
- The AI takes responsibility for tasks it performs well (content generation, adaptive difficulty, immediate feedback)
- The human retains responsibility for tasks requiring judgment (goal-setting, strategy selection, claim evaluation, self-assessment)
- The distribution is visible to both parties (via the Learner Cockpit)
- The distribution can be adjusted by the learner

This draws on:
- **Distributed Cognition** (Hutchins) — cognitive labor distributed across human and artifact
- **Human–AI Teaming** (Kamar, Horvitz) — complementary strengths of human and AI
- **Cognitive Apprenticeship** (Collins, Brown, Newman) — scaffolding that fades as learner competence grows

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Governs** | CRG governs the responsibility distribution, preventing inappropriate delegation |
| C2 Cognitive Safety | **Requires balance** | Safe cognitive labor distribution prevents overload of either party |
| C3 Instructional Integrity | **Depends on** | Reliable AI instructional actions are required for appropriate delegation |
| C4 Learner Agency | **Defines** | Agency defines what the human retains; shared responsibility defines what is delegated |
| C8 Learner Cockpit | **Displayed in** | The Learner Cockpit shows the current responsibility distribution |

### Example Observations

- **Appropriate distribution:** The AI generates practice problems and provides immediate feedback on correctness.
The learner decides which topics to focus on, how long to study, and when to seek deeper explanation.
The Learner Cockpit shows: "AI: problem generation, feedback | You: topic selection, pacing, depth."
- **Inappropriate distribution:** The AI selects topics, sets session duration, generates problems, provides feedback, and decides when the learner has "mastered" a concept — all without learner input or visibility into the decisions.
- **Appropriate negotiation:** The AI recommends spending more time on a weak topic.
The learner overrides: "I want to move on and come back to this later."
The AI accepts and documents the decision.
- **Inappropriate delegation:** The AI presents a factual claim without source attribution, and the learner accepts it without verification — epistemic labor inappropriately delegated to the AI.

### Future Benchmark Dimensions

- Responsibility distribution visibility: Does the learner know what the AI is doing and what they are expected to do?
- Delegation appropriateness: Is the AI performing tasks suitable for AI, and is the human performing tasks suitable for humans?
- Negotiation frequency: How often does the responsibility distribution change based on learner initiative?
- Accountability clarity: When something goes wrong, is it clear whether the AI or the human is responsible?

---

## C6: Transition Integrity

### Definition

The preservation of cognitive continuity, epistemic orientation, and learner agency during transitions between instructional states — lessons, topics, difficulty levels, modalities, or human–AI responsibility distributions.

Transition Integrity has three protected properties:

| Property | Description |
|----------|-------------|
| **Cognitive continuity** | The learner's working memory representation of the current topic is maintained, not disrupted, during the transition |
| **Epistemic orientation** | The learner understands how the new state relates to what they just learned — what connects, what differs, what builds upon |
| **Learner agency** | The learner is aware that a transition is occurring, understands why, and has the opportunity to influence it |

### Theoretical Motivation

Transitions are the most common and most dangerous sites of governance failure in AI-native educational systems.

Why transitions are dangerous:

- **Working memory reset:** A transition (e.g., from video to quiz, from topic A to topic B) can flush the learner's current working memory contents, destroying the mental model they were constructing
- **Context loss:** The AI may change context without the learner realizing, leading to confusion about what is being discussed
- **Agency bypass:** Transitions often happen automatically (auto-advance, difficulty change), bypassing learner choice
- **Epistemic discontinuity:** The new content may contradict, contradict, or fail to connect with the previous content, without explicit bridging

Transition Integrity draws on:
- **Cognitive continuity** (learning transfer literature) — the importance of connecting new knowledge to existing knowledge
- **Signaling theory** (Mayer) — the importance of explicit cues about structure and transitions
- **Activity theory** (Engeström) — the role of transitions between activity systems

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Governed by** | CRG applies specific transition-governance constraints |
| C2 Cognitive Safety | **Protects during** | Transition Integrity protects Cognitive Safety at the most vulnerable moments |
| C3 Instructional Integrity | **Sub-dimension of** | Transition Integrity is one of the six dimensions of Instructional Integrity |
| C4 Learner Agency | **Preserved during** | Agency must not be bypassed during transitions |
| C9 PRGW | **Spans** | The PRGW ensures no transition occurs outside the governance window |

### Example Observations

- **High integrity transition:** The system announces: "Next, we will apply the concept of gradient descent to neural networks.
This builds on the optimization framework you just learned.
Would you like a brief review before we proceed?"
- **Low integrity transition:** The system automatically advances from a lesson on linear regression to a quiz on support vector machines without any explanation of the relationship, leaving the learner wondering why the topic changed.
- **High integrity transition:** When changing difficulty, the system explains: "I'm reducing the difficulty because you missed the last two questions.
Let's review the concept with a simpler example."
- **Low integrity transition:** The video ends, a quiz appears 500ms later with no visual or textual bridge, different font, different layout — the learner is disoriented and takes 30 seconds to understand what is being asked.

### Future Benchmark Dimensions

- Transition announcement rate: What percentage of transitions include explicit explanation?
- Transition agency preservation: What percentage of transitions allow learner choice?
- Cognitive continuity score: Post-transition quiz scores on pre-transition content
- Epistemic bridging quality: Rated clarity of explanation connecting old and new content

---

## C7: Runtime Intervention

### Definition

An action triggered in real time by the detection of a governance violation, cognitive safety risk, or instructional integrity failure, designed to restore safe and effective learning conditions.

Runtime Interventions are classified by trigger and severity:

| Trigger Category | Example Triggers | Typical Interventions |
|-----------------|-----------------|----------------------|
| **Cognitive Safety** | Overload detected, confusion sustained >30s, frustration spike | Pause, simplify, offer break, change modality |
| **Instructional Integrity** | Hallucination detected, inconsistency flagged, assessment error | Correction, clarification, apology, escalation |
| **Agency Erosion** | Auto-advance without consent, override blocked, choice removed | Restore choice, explain decision, offer undo |
| **Transition Failure** | Abrupt topic change, missing bridge, modality switch without warning | Insert bridge, explain connection, offer review |
| **Shared Responsibility** | AI makes claim without uncertainty marker, epistemic labor hidden | Add uncertainty marker, request verification, display source |

### Theoretical Motivation

Runtime Intervention operationalizes the preventive aspect of Constitutional Runtime Governance.
Without intervention, governance is merely detection — it identifies problems but does not solve them.
Effective intervention requires:

- **Appropriate timing:** Intervention must occur before harm compounds, not after the learner has already been confused or frustrated for an extended period
- **Appropriate severity:** Minor issues warrant gentle interventions (clarification, hint); major issues warrant strong interventions (pause, reset, human escalation)
- **Appropriate transparency:** The learner should understand that an intervention occurred and why
- **Minimal disruption:** The intervention should restore safety without derailing learning

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Triggered by** | CRG violation detection triggers Runtime Intervention |
| C2 Cognitive Safety | **Restores** | Interventions restore Cognitive Safety when it is threatened |
| C8 Learner Cockpit | **Displayed in** | Interventions are logged and displayed in the Learner Cockpit |
| C9 PRGW | **Occurs within** | All interventions occur within the PRGW |

### Example Observations

- **Effective intervention:** The system detects three consecutive errors and intervenes: "It looks like this concept is challenging.
Would you like me to explain it differently, show a worked example, or let you take a break and come back?"
- **Ineffective intervention:** The system detects an error and responds with "Incorrect." — technically an intervention (feedback), but fails to restore safe learning conditions.
- **Transparent intervention:** The Learner Cockpit displays: "Intervention: Difficulty reduced (reason: 3 consecutive errors)."
- **Opaque intervention:** The difficulty changes without explanation, leaving the learner confused about why the content suddenly got easier.

### Future Benchmark Dimensions

- Intervention latency: Time from detection to intervention
- Intervention appropriateness: Expert rating of whether the intervention matches the severity and type of issue
- Intervention effectiveness: Post-intervention restoration of safe learning conditions
- Intervention transparency: Learner comprehension of why the intervention occurred

---

## C8: Learner Cockpit

### Definition

A persistent, learner-visible interface element that displays real-time information about the AI system's state, confidence, limitations, and governance status, enabling informed oversight and agency.

The Learner Cockpit displays:

| Information Category | Example Displays |
|---------------------|-----------------|
| **AI State** | "Currently generating an explanation" / "Waiting for your input" |
| **Confidence** | "High confidence" / "Moderate confidence — please verify" / "Low confidence — this is my best understanding" |
| **Limitations** | "I cannot access external websites" / "My knowledge was last updated in April 2024" |
| **Governance Status** | "All systems governed" / "Caution: difficulty adjusted automatically" |
| **Responsibility Distribution** | "AI: content, feedback | You: goals, pacing, verification" |
| **Recent Interventions** | "14:32: Difficulty reduced (3 errors)" / "14:45: Transition explained" |
| **Cognitive Safety Indicators** | Current load level, session duration, break reminders |

### Theoretical Motivation

The Learner Cockpit addresses a fundamental asymmetry in AI-native educational systems: the AI has perfect information about its own state, while the learner has none.
This asymmetry undermines:

- **Trust calibration:** Learners cannot calibrate appropriate trust without knowing the AI's confidence and limitations
- **Agency:** Learners cannot make informed decisions without knowing what the AI is doing and why
- **Shared responsibility:** The responsibility distribution is invisible, making accountability impossible
- **Safety monitoring:** Learners cannot recognize when they are at risk without real-time safety indicators

The Learner Cockpit concept draws on:
- **Transparency in AI** (Langer et al., Eslami et al.) — the importance of making AI behavior visible
- **Metacognitive scaffolding** (Azevedo, Jacobson) — supporting learners' awareness of their own learning process
- **Situation awareness** (Endsley) — the importance of understanding system state for effective human–machine interaction

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Displays** | The Learner Cockpit is the primary display mechanism for CRG state |
| C2 Cognitive Safety | **Monitors** | Displays real-time Cognitive Safety indicators |
| C4 Learner Agency | **Enables** | Provides the transparency needed for informed agency |
| C5 Human–AI Shared Responsibility | **Visualizes** | Shows the current responsibility distribution |
| C7 Runtime Intervention | **Logs** | Records recent interventions and their rationale |

### Example Observations

- **Present:** A sidebar displays: "AI confidence: High | Topic: Gradient Descent | Your progress: 3/5 concepts | Last intervention: None | Take a break?" — the learner has situational awareness.
- **Absent:** The interface shows only the current question and a chat input — the learner has no information about what the AI knows, what it doesn't know, what decisions it has made, or what responsibilities they retain.

### Future Benchmark Dimensions

- Information completeness: What percentage of recommended cockpit information is displayed?
- Comprehensibility: Can learners accurately interpret cockpit information?
- Utility: Does cockpit information lead to better learning decisions?
- Non-intrusiveness: Does the cockpit avoid distracting from learning?

---

## C9: Persistent Runtime Governance Window

### Definition

The continuous temporal scope within which Constitutional Runtime Governance operates — from the initiation of a learning session through all instructional transitions to session conclusion — ensuring no ungoverned instructional interval.

The PRGW has three boundaries:

| Boundary | Definition |
|----------|-----------|
| **Opening** | The moment the learner begins a learning session; governance activates |
| **Internal coverage** | All instructional actions (content, scaffolding, assessment, feedback, navigation, transitions) within the session |
| **Closing** | The moment the session ends; governance generates a summary and any deferred interventions |

### Theoretical Motivation

Governance gaps occur when CRG is not active during specific instructional intervals.
Common gap sites:

- **Session opening:** Before the learner has engaged with content, the system may make decisions (topic selection, difficulty setting) without governance
- **Transitions:** Between lessons, topics, or modalities, there may be brief intervals where governance rules are not applied
- **Session closing:** At session end, summary generation and progress reporting may lack governance
- **Background processes:** Adaptive algorithms running in the background (spaced repetition scheduling, knowledge graph updates) may operate outside the governance window

The PRGW ensures that governance is **persistent** — continuously active, not intermittently applied.

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Scope of** | The PRGW defines when and where CRG operates |
| C6 Transition Integrity | **Spans** | The PRGW extends across all transitions, preventing governance gaps |
| C7 Runtime Intervention | **Occurs within** | All interventions occur within the PRGW |
| C8 Learner Cockpit | **Displays** | The Learner Cockpit shows the PRGW status |

### Example Observations

- **Full coverage:** From the moment the learner opens the app to the moment they close it, every AI action is governed, every transition is monitored, and the Learner Cockpit shows "Governance: Active" throughout.
- **Gap detected:** The system auto-schedules the next lesson during session close, outside the learner's awareness and without governance review — a PRGW gap.

### Future Benchmark Dimensions

- Coverage percentage: What percentage of the session duration is within the PRGW?
- Gap detection: Can gaps (ungoverned intervals) be identified and measured?
- Gap severity: What instructional actions occur during gaps?

---

## C10: Governance Benchmark

### Definition

A reproducible, standardized measurement instrument designed to evaluate the extent to which an AI-native educational system adheres to Constitutional Runtime Governance principles across defined dimensions.

A Governance Benchmark has five components:

| Component | Description |
|-----------|-------------|
| **Construct alignment** | The benchmark measures a clearly defined construct (from the CRG-ANL construct ontology) |
| **Operationalization** | The construct is translated into observable, measurable indicators |
| **Scoring rubric** | A standardized method for converting observations into scores |
| **Severity classification** | A framework for classifying the severity of governance failures |
| **Reproducibility protocol** | Documentation enabling independent researchers to apply the benchmark and obtain comparable results |

### Theoretical Motivation

Without benchmarks, governance claims are untestable.
A system can claim to be "governed" or "safe" without any empirical basis.
Governance Benchmarks make these claims falsifiable by:

- Defining what "governed" means operationally
- Specifying how to observe and measure governance
- Providing a standardized scoring method
- Enabling comparison across systems, versions, and time

Governance Benchmarks are not merely evaluation tools — they are **scientific instruments** that must be validated for reliability, validity, and sensitivity.

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Evaluates** | Benchmarks measure CRG adherence |
| C2 Cognitive Safety | **Measures** | Safety benchmarks measure Cognitive Safety outcomes |
| C3 Instructional Integrity | **Measures** | Integrity benchmarks measure Instructional Integrity |
| C11 Researcher-as-Subject | **Applied through** | Benchmarks are applied by the researcher-as-subject |

### Example Observations

- **Benchmark application:** The researcher observes 10 learning sessions, codes all instructional events using the observation schema, applies the Instructional Integrity benchmark, and obtains a score of 0.72 (Good) with detailed subscores for each dimension.
- **Benchmark comparison:** Version 1.2 of the AI tutoring system scores 0.68 on the Cognitive Safety benchmark; Version 1.3 scores 0.79 — the benchmark detects the improvement.

### Future Benchmark Dimensions

- Inter-rater reliability: Do independent researchers obtain similar scores?
- Test-retest reliability: Are scores stable across repeated applications?
- Sensitivity: Can the benchmark detect meaningful differences between systems or versions?
- Validity: Does the benchmark measure what it claims to measure?

---

## C11: Researcher-as-Subject

### Definition

A methodological framework in which the researcher systematically studies their own learning experience within an AI-native educational environment, using structured observation, validated instruments, and rigorous analytical protocols to generate evidence about Constitutional Runtime Governance, Cognitive Safety, Instructional Integrity, and related constructs.

The Researcher-as-Subject framework has six components:

| Component | Description |
|-----------|-------------|
| **Structured observation** | Pre-defined observation protocols that guide what to notice, record, and code during learning sessions |
| **Validated instruments** | Standardized measurement tools (NASA-TLX, subjective scales, interaction logs) applied consistently |
| **Analytical protocol** | Pre-defined procedures for analyzing observations, applying benchmarks, and drawing conclusions |
| **Bias mitigation** | Explicit procedures for identifying and mitigating researcher-specific biases (confirmation bias, expectation effects, Hawthorne effect) |
| **Evidence documentation** | Systematic recording of observations in a canonical format (the observation schema) |
| **Adversarial review** | Independent critique of methods, findings, and conclusions |

### Theoretical Motivation

Researcher-as-Subject methodology is necessary for CRG-ANL research because:

- **Ethical constraints:** Subjecting other learners to experimental observation of their cognitive states and AI interactions raises significant privacy and consent issues
- **Granularity:** Only the researcher can access their own internal cognitive states (confusion, overload, frustration) with the precision needed for Cognitive Safety measurement
- **Expertise:** The researcher's domain expertise enables sophisticated evaluation of Instructional Integrity (detecting subtle errors, inconsistencies, and pedagogical failures that non-experts might miss)
- **Access:** The researcher has legitimate access to the educational platform as a enrolled student

Researcher-as-Subject is not a methodological weakness to be apologized for.
It is a **deliberate design choice** with distinct epistemic advantages, provided it is executed with rigorous protocols for validity, bias mitigation, and reproducibility.

The methodology draws on:
- **N-of-1 trials** (Guyatt, Zucker) — rigorous single-subject experimental designs
- **Autoethnography** (Ellis, Adams) — systematic self-study as research methodology
- **Experience sampling** (Csikszentmihalyi, Larson) — capturing real-time subjective experience
- **Self-experimentation** (Roberts) — rigorous experimental design applied to oneself

### Relationships

| Relates To | Nature | Description |
|-----------|--------|-------------|
| C1 CRG | **Studies** | Researcher-as-Subject generates evidence about CRG in practice |
| C10 Governance Benchmark | **Applies** | The researcher applies Governance Benchmarks to their own learning experience |
| All constructs | **Generates evidence for** | All constructs are investigated through researcher-as-subject methodology |

### Example Observations

- **Methodology in action:** The researcher completes a Quantic lesson while recording: NASA-TLX ratings (mental demand: 75/100), subjective scales (transparency: 3/7, agency: 4/7), interaction log (12 AI exchanges, 2 detected scaffolding errors, 1 abrupt transition), and structured notes ("The AI explained gradient descent using chain rule notation before introducing the chain rule concept — scaffolding integrity failure").
- **Bias mitigation:** Before analyzing Pilot 001 data, the researcher documents their prior expectation that Quantic's AI tutoring system will score poorly on Transition Integrity.
This expectation is recorded in the decision log and referenced during analysis to guard against confirmation bias.

### Future Benchmark Dimensions

- Protocol fidelity: How closely does the researcher follow the structured observation protocol?
- Inter-rater reliability (where applicable): When observations are independently coded, what is the agreement rate?
- Validity evidence: Do researcher-as-subject findings converge with other data sources where available?
- Methodological refinement: How can the protocol be improved based on pilot experience?
