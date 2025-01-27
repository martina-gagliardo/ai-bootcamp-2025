# Scrivere il codice dell'esercizi qui dentro
from python.giorno2_3.esercizi.funzioni.crash import factorial


def mydivmod(a,b):
    if b == 0:
        print("Non puoi dividere per zero")
    quoziente = a // b
    resto = a % b
    return quoziente, resto

print(mydivmod(10, 3))


def pow_list(my_list):
    return [x ** 2 for x in my_list]

def count_words(word):
    word_length = word.split(' ')
    return len(word_length)

print(count_words('hello world'))

def reverse_string(x):
    return x[::-1]

mytxt = reverse_string("hello")
print(mytxt)

def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    return n * fattoriale(n - 1)
print(fattoriale(5))


def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))


def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
print(sum_even_numbers([1, 2, 3, 4, 5]))


def find_max(numbers):
    return max(numbers)
print(find_max([3, 1, 4, 1, 5]))

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
print(count_vowels("hello world"))








































