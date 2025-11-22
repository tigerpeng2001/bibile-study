# Edit Furigana via Field Codes in MS Word (Mac)

This guide explains how to edit Japanese **振り仮名 (furigana / ruby text)** using **field codes** in **Microsoft Word for Mac**, specifically when furigana is stored using `EQ` fields.

---

## 🔍 Example of Ruby in Field Code Format

---

## 📌 Field Components Overview

Here is a breakdown of the major switches you may see in an EQ-based furigana field:

| Component | Meaning | Notes |
|-----------|---------|-------|
| `\o` | Overstrike (stack elements vertically) | Used to place ruby above base text |
| `\ad` | Alignment adjustment | Centers stacked elements based on font metrics |
| `\up N` | Raise text by N points | Controls vertical spacing between furigana and kanji |
| `\dn N` | Lower text by N points | Opposite of `\up` |
| `\sN` | Scales text to N% | Often used to shrink ruby text |
| `\hpsN` | Sets font size in half-points | Example: `hps20` = 10pt |
| `\* jc2` | Inline centered justification | Keeps furigana centered above character |
| `\* jc0` | Left alignment | |
| `\* jc1` | Center relative to page margins | Behaves like centered equation |
| `\* jc3` | Right alignment | |
| `\* "Font:…"` | Forces a specific font | Useful when furigana uses different font from text |

Example field:

```
{ EQ \* jc2 \* "Font:Microsoft YaHei" \* hps20 \o\ad(\s\up 12(き),木) }
```

---

## 🧩 Explanation of `\* jc2`

- `jc` = justification
- `2` = center relative to inline text (not page margins)

This keeps ruby centered above the character rather than behaving like a block equation.

**Without `jc2` (may drift):**
```
{ EQ \o\ad(\s\up 12(き),木) }
```

**With `jc2` (recommended):**
```
{ EQ \* jc2 \o\ad(\s\up 12(き),木) }
```

---


### **What `\ad` Means**

In EQ field syntax, `\ad` is an alignment adjustment modifier used with `\o` (overstrike). It attempts to visually center stacked elements (furigana vs. base text) by compensating for font metrics.

- With `\o` only → positioning may look misaligned
- With `\o\ad` → Word centers elements more accurately

Example:

```
{ EQ \o(\s\up 10(き),木) }      ← may be misaligned
{ EQ \o\ad(\s\up 10(き),木) }  ← better centering
```

`\ad` does **not** control spacing; it only affects alignment.

---

## 🔍 Example of Ruby in Field Code Format

When you toggle field codes (`Shift + F9`), ruby may appear like this:

```
{ EQ \* jc2 \* "Font:Microsoft YaHei" \* hps20\o\ad(\s\up 12(き),木) }
```

This format uses **Equation field syntax** rather than the Windows-style `JA()` phonetic guide.

---

## 🔧 Meaning of Key Components

| Code | Meaning |
|------|---------|
| `EQ` | Equation field |
| `\o` | Overstrike (stack characters vertically) |
| `\ad` | Adjust alignment |
| `\s` | Scale text size |
| `\up 12` | Move ruby text upward by 12pt |
| `(き),木` | First = ruby, second = base character |

---

## ✏ Adjusting Space Between Kanji & Furigana

The vertical spacing is controlled by the `\up` value.

### **Decrease Space (Closer)**

```
\up 8(き)
```

### **Increase Space (Further Apart)**

```
\up 16(き)
```

### Example

**Before:**
```
{ EQ \* jc2 \* "Font:Microsoft YaHei" \* hps20\o\ad(\s\up 12(き),木) }
```

**After (tighter):**
```
{ EQ \* jc2 \* "Font:Microsoft YaHei" \* hps20\o\ad(\s\up 8(き),木) }
```

Toggle back using `Shift + F9` to display normally.

---

## 🎛 Other Useful Adjustments

### **Change Ruby Font Size**

```
\s18(き)  → larger
\s12(き)  → smaller
```

### **Horizontal Alignment Variants**

| Code | Effect |
|------|--------|
| `\al` | Left align |
| `\ac` | Center align |
| `\ar` | Right align |

Example:
```
\o\ad\ac(...)
```

---

## ⚠ Limitations in Mac Word

| Feature | Mac Word | Windows Word (Japanese) |
|---------|----------|-------------------------|
| Automatic ruby from phonetic guide | ❌ | ✔ |
| `JA()` ruby field support | ❌ | ✔ |
| Character-by-character control via EQ fields | ✔ | ✔ |

Mac stores ruby differently and may require manual editing.

---

## 📌 Recommended Tools for Large Ruby Documents

| Tool | Why |
|------|-----|
| **Windows Word (Japanese)** | Best automation, proper ruby handling |
| **Apple Pages** | Native ruby, easy formatting |
| **LaTeX (ruby package)** | Best typesetting control |
| **Google Docs** | Not recommended—no ruby support |

---

## ✅ Summary

- On Mac, ruby often appears as `EQ` fields using `\o` overstrike formatting
- Vertical spacing is controlled by `\up <value>`
- Smaller value → closer to base text
- Larger value → further away

---

If you want, I can also provide **batch scripts or Word macros** to convert all ruby into a consistent format.

