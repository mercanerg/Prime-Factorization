"""
------ Prime Factorization using Division Method ---
The division method can also be used to find the prime factors of a large number
by dividing the number by prime numbers. Follow the steps given below to find
the prime factors of a number by using the division method:

Step 1: Divide the number by the smallest prime number such that
the smallest prime number should divide the number completely.
Step 2: Again, divide the quotient of step 1 by the smallest prime number.
Step 3: Repeat step 2, until the quotient becomes 1.
Step 4: Finally, multiply all the prime factors that are the divisors."""

def numbercontrol():
    cond = True
    while cond:
        n = input('Enter a number you want to take out the factors --> ')
        if n.isnumeric():
            number = int(n)
            cond = False
        else:
            print("invalid number try again")
    return number

def multiple(number):
    mult = []
    for i in range(2, number+1):
        modulus = number % i
        if modulus == 0:
            mult.append(i)
    return mult

def primenumber(fract):
    multipliers = []
    for k in fract:
        prime = True
        for j in range(2,k):
              mod = k % j
              if mod == 0:
                  prime = False
        if prime:
            multipliers.append(k)
    return multipliers

def divider(listed, sayi):
  result = ''
  for n in listed:
      durum = True
      c = 0
      while durum:
          mod = sayi % n
          div = sayi // n
          if mod == 0:
              c += 1
              sayi = div
          else:
              if n==listed[len(listed)-1]:
                  result += f"{n}^{c}"
              else:
                  result += f"{n}^{c} x  "
              durum = False

  return result
number = numbercontrol()
print(number)
divisor = multiple(number)
fraction_list = primenumber(divisor)
res = divider(fraction_list, number)

print(f"\ndivisors of {number} : {divisor}\n")
print(f"prime factors of  {number} : {fraction_list}\n")
print(f"{number} = {res}\n")
