import module_b
import module_a

print '5 * 3 =', module_b.triple(5)
print '5 * 2 =', module_a.double(5)

print 'Access module a from module b', module_b.module_a.__name__