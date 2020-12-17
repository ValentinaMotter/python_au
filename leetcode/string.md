+ [Valid Anagram](#)
+ [Reverse String](#)
+ [Reverse Vowels of a String](#)
+ [Reverse Words in a String III](#)
+ [To Lower Case](#)
<!-----solution----->

## To Lower Case



```python

def toLowerCase(self, str: str) -> str:
    return "".join(chr(ord(i) + 32) if 65 <= ord(i) <= 90 else i for i in str)
```

## Reverse Words in a String III



```python

def reverseWords(self, s: str) -> str:
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)
```

## Reverse Vowels of a String



```python

def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels and s[right] not in vowels:
            right -= 1
        elif s[left] not in vowels and s[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s)
```

## Reverse String



```python

def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
```

## Valid Anagram



```python

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```