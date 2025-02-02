# Regular Expression (RegEx) Pattern Cheat Sheet

Here's a **Regular Expression (RegEx) Pattern Cheat Sheet** to help you quickly reference common patterns.  

---

## **1. Basic Characters**  

| Pattern | Description |
|---------|------------|
| `.` | Matches **any** character except a newline |
| `a` | Matches the **character 'a'** |
| `abc` | Matches the **exact sequence** "abc" |

---

## **2. Character Classes**  

| Pattern | Description |
|---------|------------|
| `[abc]` | Matches **'a' or 'b' or 'c'** (any character inside brackets) |
| `[^abc]` | Matches any character **except 'a', 'b', or 'c'** |
| `[a-z]` | Matches **any lowercase letter** |
| `[A-Z]` | Matches **any uppercase letter** |
| `[0-9]` | Matches **any digit** |
| `[a-zA-Z0-9]` | Matches **any letter or digit** |
| `\d` | Matches **any digit (0-9)** (same as `[0-9]`) |
| `\D` | Matches **any non-digit** (same as `[^0-9]`) |
| `\w` | Matches **any word character** (`[a-zA-Z0-9_]`) |
| `\W` | Matches **any non-word character** (`[^a-zA-Z0-9_]`) |
| `\s` | Matches **any whitespace** (space, tab, newline) |
| `\S` | Matches **any non-whitespace character** |

---

## **3. Quantifiers**  

| Pattern | Description |
|---------|------------|
| `a*` | Matches **0 or more** occurrences of 'a' |
| `a+` | Matches **1 or more** occurrences of 'a' |
| `a?` | Matches **0 or 1** occurrence of 'a' (optional) |
| `a{3}` | Matches **exactly 3** occurrences of 'a' |
| `a{2,5}` | Matches **between 2 and 5** occurrences of 'a' |
| `a{2,}` | Matches **2 or more** occurrences of 'a' |

---

## **4. Anchors**  

| Pattern | Description |
|---------|------------|
| `^abc` | Matches "abc" **at the beginning** of a line |
| `abc$` | Matches "abc" **at the end** of a line |
| `\bword\b` | Matches the **whole word** "word" (word boundary) |
| `\Bword\B` | Matches "word" **inside another word** (no boundary) |

---

## **5. Groups & Alternation**  

| Pattern | Description |
|---------|------------|
| `(abc)` | Capturing group (treats "abc" as a single unit) |
| `(a\|b\|c)` | Matches **'a' or 'b' or 'c'** |
| `(?:abc)` | Non-capturing group (groups without capturing) |

---

## **6. Lookaheads & Lookbehinds**  

| Pattern | Description |
|---------|------------|
| `a(?=b)` | Matches 'a' **only if followed by 'b'** (positive lookahead) |
| `a(?!b)` | Matches 'a' **only if NOT followed by 'b'** (negative lookahead) |
| `(?<=b)a` | Matches 'a' **only if preceded by 'b'** (positive lookbehind) |
| `(?<!b)a` | Matches 'a' **only if NOT preceded by 'b'** (negative lookbehind) |

---

## **7. Escape Sequences**  

| Pattern | Description |
|---------|------------|
| `\.` | Matches **a literal dot (.)** |
| `\*` | Matches **a literal asterisk (*)** |
| `\\` | Matches **a literal backslash (\)** |
| `\n` | Matches **a newline** |
| `\t` | Matches **a tab** |

---

## **8. Common Patterns**  

| Pattern | Description |
|---------|------------|
| `^\d{4}$` | Matches a **4-digit number** (e.g., `2024`) |
| `^\w+@\w+\.\w+$` | Matches a **basic email** (e.g., `test@mail.com`) |
| `\b\d{10}\b` | Matches a **10-digit phone number** |
| `https?://\S+` | Matches **URLs** (`http://` or `https://`) |
| `#[A-Fa-f0-9]{6}` | Matches **hex color codes** (e.g., `#FFA500`) |

---

This cheat sheet covers the essentials! Do you need help with a specific pattern? 🚀
