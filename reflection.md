# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game did not run properly. At first it seems to work, if you don't know what the "secret" number is supposed to be, but the hints telling you which way to guess (higher or lower) do not work properly. If you guess above the target range, it tells you to guess higher, and if you guess below the target range it tells you to guess lower, both of which don't make sense.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The main bugs I noticed immediately were the incorrect hints, in both directions, and the scoring also seemed to be inconsistent. Each time I didn't guess the correct number, the score would be different. I also noticed that the new game button doesn't actually restart the game. The only way to try again was to refresh the page entirely.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project I used Claude. I couldn't figure out how to load it into the terminal, so I was using Copilot at first, but I figured it out eventually, and all of my debugging assistance was with Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI solution to the reversed hints was correct and worked in the program. It suggested the swapping of the code in each part of the if statement. This was relatively easy to verify because it was a pretty simple fix, and I was easily able to understand exactly how the solution worked.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At first the test cases that Claude suggested did not properly test the logic of the fixed bugs, which was confusing when looking at the results. After opening a new chat and retrying, the tests were able to effectively test the code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested if a bug was fixed, by first understanding what exactly was wrong and what needed to be changed, verifying Claude's solution. Then I ran test cases, which helped verify that the fix worked for specific values, then finally I tested the game itself to make sure the changes translated there.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran tests in pytest that tested what the outcome of the variable that displayed the hint was, when the guessed value was either higher or lower than the secret value. Through this test case, I was able to verify that the correct hints would appear, depending on the input value.
- Did AI help you design or understand any tests? How?
Yes, I used AI to write the original test cases, some of which did not work properly, which then allowed me to check what did and did not properly test the code. By figuring this out, I was able to rewrite those test cases to effectively test the bug fixes. Using AI to write the original test cases, gave me more of a base understanding and was helpful for creating test cases of my own.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
In Streamlit, the entire script reruns from top to bottom every time there's user interaction (like a button click or input change). Without session state, variables like the secret number were being recalculated on each rerun, generating a new random number instead of keeping the same one throughout the game. This meant the target was constantly changing as the player tried to guess it.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine you're running a recipe while someone keeps interrupting you. Every time they interrupt, you start the recipe from the beginning. Streamlit works the same way—each time a user clicks a button or types something, it reruns your entire script from top to bottom. Session state is like writing down ingredients on a sticky note so they don't get lost between reruns. Without it, the app forgets everything and recalculates from scratch, which is why your secret number was changing. Session state keeps important data (like your secret number) persistent across all those reruns, so the game stays consistent.
- What change did you make that finally gave the game a stable secret number?
I stored the secret number in Streamlit's `session_state` dictionary, so it persists across reruns instead of being recalculated every time the user interacts with the app. This way, the same number stays constant throughout the entire game session until the player clicks the "New Game" button to explicitly generate a new one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I found the process of utilizing both my own knowledge of debugging and the AI suggestions simultaneously very helpful. I've never used embedded AI with coding before and I'm looking forward to finding new ways to utillize it.
- What is one thing you would do differently next time you work with AI on a coding task?
I think in certain parts I could have depended less on the AI, specifically with the bug fixes, I think there is more room for collaboration than I used with this project.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project allowed me to see AI code as more of a means of assistance than "cheating" or just having the answers handed to you. 
