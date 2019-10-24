start = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]



rosnące = sorted(start, key=lambda x: x[1])

# pierwsza próba bez czytania dokumentacji, nie działała, łączyła wszystko w jedeną długą listę. drugie podejście było po czytaniu dokumentacji.
# first1=start[0]
# first2=first1[::-1]

# second1=start[1]
# second2=second1[::-1]

# third1=start[2]
# third2=third1[::-1]

# fourth1=start[3]
# fourth2=fourth1[::-1]

# fifth1=start[4]
# fifth2=fifth1[::-1]

# sixth1=start[5]
# sixth2=sixth1[::-1]

# seventh1=start[6]
# seventh2=seventh1[::-1]

# eight1=start[7]
# eight2=eight1[::-1]

# nineth1=start[8]
# ninenth2=nineth1[::-1]

# tenth1=start[9]
# tenth2=tenth1[::-1]

# z=[]
# z.extend(first2)
# z.extend(second2)
# z.extend(third2)
# z.extend(fourth2)
# z.extend(fifth2)
# z.extend(sixth2)
# z.extend(seventh2)
# z.extend(eight2)
# z.extend(ninenth2)
# z.extend(tenth2)
print(rosnące)