# by Yuhang Wu 5/31/19 9:11 am
a = 'Yuhang Wu'
b = 10 # not a lie
c = 54 # inches
d = 85 # pounds
e = 'Brown'
f = 'White'
g = 'Black'

print "Let's talk about %s." % a
print "He is %d inches tall." % c
print "He's %d pounds heavy." % d
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (e, g)
print "His teeth are usually %s depending on his milk." % f

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    b, c, d, b + c + d)
