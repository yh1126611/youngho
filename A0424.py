a, b, c = map(int, input().split())

root_1 = -(b/(2*a)) + ((((b*b)-(4*a*c))**(1/2))/(2*a))
root_2 = -(b/(2*a)) - ((((b*b)-(4*a*c))**(1/2))/(2*a))

print("BAAM! Here are the roots: %.2f and %.2f." % (root_1, root_2))