import theano
import theano.tensor as T
import theano.printing
k = T.iscalar("k")
a = T.dscalar("a")
result, updates = theano.scan(fn=lambda prior_result, a: prior_result * a, outputs_info=a,
non_sequences=a, n_steps=k-1)
final_result = result[-1]
a_pow_k = theano.function(inputs=[a,k], outputs=final_result, updates=updates)
print(a_pow_k(2,5), 2 ** 5)
