# Daniel A. Herrmann — Radical AI Interpretability

## Summary

Herrmann asks how we could work out what an AI system believes or wants by combining what it does with evidence from inside the system. He argues that these two approaches can help each other, but warns that researchers may misunderstand the system if they assume it organizes ideas exactly as people do. The photographed slides are a partial record of the presentation, not a complete transcript of the talk.

## 061 — Radical AI Interpretability

### Visible text

Radical AI Interpretability  
Daniel A. Herrmann  
Minds, Meaning, and Machines  
UNC Chapel Hill

### In everyday language

This is the title slide. The talk asks how we might interpret what is going on inside an AI system.

## 062 — Radical AI Interpretability

### Visible text

Radical AI Interpretability  
Daniel A. Herrmann  
Minds, Meaning, and Machines  
UNC Chapel Hill

### In everyday language

A second photograph of the title slide.

## 063 — Lewis and radical interpretation

### Visible text

Radical Interpretation  
Lewis (1974)

The slide presents Lewis's thought experiment about interpreting Karl from physical facts, and asks how his beliefs, desires and meanings can be determined from those facts.

### In everyday language

Imagine you know all the physical facts about a person but are not told what they believe, want, or mean. How could you work those things out? This is the starting puzzle. The small quotation is not reliably legible enough here for a complete word-for-word transcription.

## 064 — Adapting the thought experiment

### Visible text

Radical Interpretation, adapted for AI

The slide adapts the preceding thought experiment by replacing Karl with Claude and considering the model's architecture, weights and computational system.

### In everyday language

The same question is now applied to an AI system: given its construction and behavior, can we describe what it believes or wants? The altered example is the presenter's adaptation, not a literal quotation from Lewis. Some small text cannot be read confidently.

## 065 — Plan

### Visible text

1. Radical interpretation, adapted for AI
2. Two routes in: representationalism and interpretationism
3. Criteria for belief and desire, at a glance
4. Propositions: the projection problem
5. Ways forward

### In everyday language

The talk moves from the basic puzzle to two ways of investigating it, then considers how researchers might accidentally project human categories onto AI. This image is a video preview; only the visible frame is transcribed.

## 066 — Plan

### Visible text

1. Radical interpretation, adapted for AI
2. Two routes in: representationalism and interpretationism
3. Criteria for belief and desire, at a glance
4. Propositions: the projection problem
5. Ways forward

### In everyday language

A clearer photograph of the plan shown in item 065.

## 067 — Data, goal and procedure

### Visible text

The data: All the physical facts: internals and behaviour. Nothing about belief, desire, or meaning. That is what makes it radical.

The goal: an agential description A = ⟨P, D, 𝔄⟩. P: beliefs, as probabilities; D: desires, as desirabilities; 𝔄: a Boolean algebra of propositions.

The procedure: Test candidate descriptions by how well they predict behaviour and how rational the agent looks.

### In everyday language

Start with the system's physical workings and observable actions. Then try out descriptions of what it might believe and value, checking whether those descriptions help explain its actions. The mathematical symbols are a compact way to keep track of possible claims, confidence in them, and how desirable outcomes are.

## 068 — Data, goal and procedure

### Visible text

The data: All the physical facts: internals and behaviour. Nothing about belief, desire, or meaning. That is what makes it radical.

The goal: an agential description A = ⟨P, D, 𝔄⟩. P: beliefs, as probabilities; D: desires, as desirabilities; 𝔄: a Boolean algebra of propositions.

The procedure: Test candidate descriptions by how well they predict behaviour and how rational the agent looks.

### In everyday language

This repeats the preceding slide: the proposed interpretation should make sense of what the system does, using a consistent account of its beliefs and preferences.

## 069 — Data, goal and procedure

### Visible text

The data: All the physical facts: internals and behaviour. Nothing about belief, desire, or meaning. That is what makes it radical.

The goal: an agential description A = ⟨P, D, 𝔄⟩. P: beliefs, as probabilities; D: desires, as desirabilities; 𝔄: a Boolean algebra of propositions.

The procedure: Test candidate descriptions by how well they predict behaviour and how rational the agent looks.

### In everyday language

Another photograph of the same slide. “Rational” here refers to how well the proposed beliefs and preferences fit the actions, not a claim that the AI thinks like a person.

## 070 — Two routes to interpretation

### Visible text

Agential description A; Behaviour; Computational system.

Describes (interpretationism); Describes (representationalism). Informs/Constrains (representation theorems); Informs/Constrains (mechanistic interpretability).

Radical interpretation: get all three to cohere.

### In everyday language

One route looks at what the system does; another looks inside the machinery. Herrmann suggests that a good account should fit both kinds of evidence. The diagram connects the system, its behavior, and a description of its apparent beliefs and aims.

## 071 — Looking inside a machine

### Visible text

The slide quotes Robert Stalnaker, *Inquiry*, p. 16, about a machine whose behavior fits two competing explanations even though there is a fact about how the machine works internally.

### In everyday language

Two explanations can predict the same outward behavior. Inspecting the machinery may help us decide which explanation better fits what is actually happening. The quotation is too small in this photograph to reproduce reliably in full.

## 072 — Looking inside a machine

### Visible text

Robert Stalnaker, *Inquiry*, p. 16. The same quotation as item 071 appears again.

### In everyday language

Another photograph of the Stalnaker quotation: observing behavior alone may leave more than one possible explanation.

## 073 — Combining the routes

### Visible text

For us, not rivals.

Many belief–desire pairs rationalize the same behaviour. Internal structure can break ties and extend reach. And what we find inside is evidence the interpretationist can use too.

### In everyday language

These approaches need not compete. If several stories about a system's beliefs and aims fit its actions, information about its internal workings may help distinguish them. This item is a video preview; only the visible frame is transcribed.

## 074 — Combining the routes

### Visible text

For us, not rivals.

Many belief–desire pairs rationalize the same behaviour. Internal structure can break ties and extend reach. And what we find inside is evidence the interpretationist can use too.

### In everyday language

A still photograph repeating the preceding point: evidence from behavior and evidence from inside the system can be used together.

## 075 — A transformer and a probe

### Visible text

A transformer, and a probe.

Each token becomes a vector. Information flows up through layers and right across tokens. A probe: a small classifier that reads a feature off an intermediate vector.

The diagram uses the example “John Keats was a poet” and labels a probe pointing to “belief.”

### In everyday language

A language model turns pieces of text into lists of numbers and processes those lists through layers. A probe is a small tool trained to look for a pattern in those numbers. Finding a pattern can be useful evidence, but by itself does not prove the system has a human-like belief.

## 076 — The linear representation hypothesis

### Visible text

The linear representation hypothesis.

Concepts are directions in activation space. (Park, Choe & Veitch 2024)

Measurement: a linear probe projects and reads off. Intervention: add the direction, and the output shifts.

The diagram illustrates a “bird direction.”

### In everyday language

One proposal is that some concepts show up as particular directions in the model's numerical activity. Researchers can look for such a direction and also change the activity to see whether the model's output changes. This is a hypothesis about some representations, not a guarantee that every concept works this way.

## 077 — OthelloGPT

### Visible text

OthelloGPT (Li et al. 2023; Nanda et al. 2023).

Trained only to predict legal moves; never told the rules or shown a board. Probes recovered board state. Intervene on the represented board and it plays the new board. Black/white probes found only nonlinear structure; mine/yours probes found a linear one.

### In everyday language

A model trained on sequences of moves in the game Othello developed internal patterns that researchers could use to recover the board. Changing those patterns could affect its next moves. How researchers described the pieces mattered: “mine” and “yours” worked differently from “black” and “white.”

## 078 — Bolker's theorem

### Visible text

Preferences ≽ over an atomless Boolean algebra 𝔄, satisfying averaging, impartiality, and continuity.

Bolker's theorem (1967): There are a probability measure P and a signed measure ν on 𝔄 such that A ≽ B ⇔ D(A) ≥ D(B), D(A) = ν(A)/P(A).

### In everyday language

This mathematical result says that, if preferences meet particular conditions, they can be represented using measures of probability and desirability. It provides a possible tool for interpreting choices; it does not establish that an AI has human desires.

## 079 — Criteria for belief and desire

### Visible text

Belief and desire: anchor, coherence, use, and uniformity.

Belief: truth; largely true on settled matters (charity); probability axioms, stability under rephrasing, logical combinations; guides outputs; one decoding scheme across domains.

Desire: intelligibility; content we can grasp, specific enough to predict with; means–ends consistency, transitivity, Jeffrey–Bolker axioms; steers means toward stable ends; novel goals readable with the same tools.

Representationalist: conditions on internal states. Interpretationist: conditions on the best theory.

### In everyday language

The table lists possible signs that a belief-and-desire description is useful: it should make sense, hang together, help predict behavior, and work consistently across cases. Someone focusing on internal representations applies these criteria to the system's workings; someone focusing on interpretation asks whether the overall explanation fits.

## 080 — Hidden assumptions in probing

### Visible text

Probing in practice: write “Lord Byron died in 1824,” label it true, train a probe.

Hidden assumptions: the model treats the sentence as truth-evaluable; its beliefs about it are ours; its logical relations are ours.

### In everyday language

Even a simple test can smuggle in assumptions. A researcher may assume that the model understands a sentence, its truth, and its relationship to other statements in the same way a person does. Those assumptions themselves need examination.

## 081 — Belief and meaning

### Visible text

“In radical interpretation […] we must somehow deliver simultaneously a theory of belief and a theory of meaning.” — Davidson, “Belief and the Basis of Meaning.”

Lewis: solve for the rest, meanings included. The propositions are output. Our methods treat them as input.

### In everyday language

To work out what someone believes, we need to know what their words or internal signals mean; to work out meaning, we may need to know what they believe. The slide argues that some AI tests assume the meanings in advance, even though discovering them is part of the problem.

## 082 — Back to Othello

### Visible text

Black/white probes found non-linear structure. Mine/yours probes found linear structure.

“One challenge with probing is knowing which features to look for. […] What might seem ‘sensible’ to a human interpreter (BLACK, WHITE) may not be for a model.” — Nanda, Lee & Wattenberg (2023).

Had they stopped at the non-linear result, they would have drawn the wrong conclusion.

### In everyday language

The same game can be described using colors or using which player owns each piece. The model's internal organization was easier to find with the latter description. A test built around a human's first guess can therefore miss a useful pattern.

## 083 — Which categories are natural?

### Visible text

The two schemes are interdefinable given a time index. Black moves first, so:

Mine: black on odd turns, white on even turns.  
Yours: white on odd turns, black on even turns.

Goodman's grue. Neither pair is more natural in logical terms. Which is natural depends on the system doing the representing.

### In everyday language

If you know whose turn it is, you can translate between “black/white” and “mine/yours.” Both describe the same game, but one may fit a particular system's internal organization better. “Grue” refers to a philosophical example showing that a category can combine familiar properties in an unfamiliar way.

## 084 — The pragmatic constraint

### Visible text

The pragmatic constraint.

Behaviour lands in our conceptual space. Alien content that never reaches behaviour we care about is irrelevant. We need enough of the algebra to predict the behaviour that matters. Context-specific prediction needs far less than universal coverage.

### In everyday language

For a practical task, we may not need to understand every internal category an AI could possibly use. We need an account that helps predict the behavior relevant to that task. The speaker presents this as a way to narrow the problem.

## 085 — A possible way forward

### Visible text

Transposed to LLMs:

Sentences ↝ sparse codes from a sparse autoencoder (?)  
Preferences ↝ attitudinal data: truth directions, candidate desire-representations.

Holism becomes an asset: a grip on any one of P, D, 𝔄 is leverage on the others.

We do not know how to do this reliably yet.

### In everyday language

The slide suggests combining tentative clues about a model's concepts, apparent judgments, and apparent preferences. A “sparse autoencoder” is one method researchers use to look for simpler patterns in complicated model activity. The question mark and final sentence signal that this is a research proposal, not a solved technique.

## 086 — Where things stand

### Visible text

A mixed outcome:

Belief has representational backing (internal vectors & causal probes). Desire remains largely interpretationist (agentic behavior, no clear internal vectors). The agentic turn strengthens the interpretationist case for both.

The algebra 𝔄 is the bottleneck: getting propositions wrong breaks every criterion at once.

We can look inside (unlike Lewis & Davidson)—the challenge is reading internal features without projecting human categories.

### In everyday language

Herrmann's conclusion is that there is some internal evidence relevant to beliefs, while evidence about desires still relies more on interpreting behavior. A major difficulty is deciding what the system's internal patterns are about without forcing them into our own categories. These are the speaker's conclusions, not settled facts.
