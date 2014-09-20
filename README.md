populated_method
=====

pre-populate a method with arguments

### Install

<pre><code>pip install git+ssh://git@github.com/will-weiss/populated_method.git@master</code></pre>

### Usage

<pre><code>from populated_method import populated_method

def f(x = None, y = None, *args, **keywords):
    print "x: %s" %(x)
    print "y: %s" %(y)
    print "args: " + str(args)
    print "keywords: " + str(keywords)

populated_f = populated_method(f, y = 3, tetherball = 20)

populated_f(zeta = 5)
populated_f('a', 'b', 'c', triumph = 22)</code></pre>

<pre><code># Output
# ------
# x: None
# y: 3
# args: ()
# keywords: {'tetherball': 20, 'zeta': 5}
# x: a
# y: 3
# args: ('b', 'c')
# keywords: {'tetherball': 20, 'triumph': 22}</code></pre>