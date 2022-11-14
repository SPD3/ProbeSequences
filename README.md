Sean Doyle
spd7416@nyu.edu

The goal of this project was to implement a probe sequence algorithm that would 
allow for all n! possible probe sequences to be generated within an array of fixed size n. This was done within 
the context of a HashMap, and main.py shows some example code of the HashMap that was created
being used.

For an array of size n, the maximum possible number of probe sequences that can 
be generated is n! if each element in the probe sequence is unique. This is 
because each element in the probe sequence eliminates 1 possible index from each 
of the following probe sequence values which results in a factorial. For 
example, in an array of size 4 the first element in a probe sequence has 4 
different options(0-3 inclusive) but once a value is picked for the first 
element, the next element only has 3 different options. If the probe sequence is
constrained to unique values which is optimal when hashing a value within an 
array this results in n! possible probe sequences.

One algorithm for generating a probe sequence on a key being hashed into an array
is to hash the key to a value less than the size of the array and then increment 
the probe sequence by 1 across all indices of the array. This algorithm does 
produce a probe sequence that covers all possible indices in the array and 
produces unique elements within the probe sequence, however, it only has the 
opportunity to generate n different probe sequences. This is because the 
starting value that the key is hashed to determines the entire probe sequence so 
the number of different probe sequences is limited to the n different possible 
values that the key can be hashed to.

The algorithm that was developed within this project was designed to cover all 
n! possible probe sequences. This was done by hashing the key being 
inserted into the HashMap to a value between 0 and n!. This value determined 
the entirety of the probe sequence, and each probe sequence generated from a 
value between 0 and n! was unique. 

The following is a description of how unique probe sequences were generated from 
the hashed value between 0-n! The hashed values was called the probe_index, and 
for each iteration from 0-n the probe index was modded by the number of possible 
indices it could generate and then integer divided by that same number. On the 
first iteration this size was n, but on each subsequent iteration the number of 
possible indices decreased by 1 until the last value in the probe sequence when 
there was only 1 possible index. The result of the modulus was not directly 
appended onto the probe sequence because this could result in indices being 
repeated. Rather a swap mem value was constructed to ensure that all indices 
generated were unique from one another. Each time an index was generated it 
would be swapped with the last possible index that could still be generated in 
order to allow for that last possible index to have an opportunity to be 
generated on subsequent iterations. The best way to understand this is with the 
following example:
Lets say there is an array with capacity 5 that a probe sequence is being generated for.
The probe_index is a value between 0 and 5! and this value will be modded and then 
integer divided by 5 in order to get the first value in the probe sequence. Let's 
say that this first value is 2 for example. We now know that the next value that 
the probe_index is going to be modded and then integer divided by will be 4 and 
that this could result in another index of 2 which would be undesirable. To fix 
this problem we swap the values of 2 and 4 so that any time a 2 is generated as 
an index in the future 4 takes it's place. Initially when we were modding and 
integer dividing by 5 there was a direct mapping between the result of the mod 
and the probe sequence integer generated, but after this first iteration we begin 
swapping indices to ensure that subsequence mods and integer divides generate 
unique probe sequence indices.
On the first iteration the result of mod directly mapped onto the following array:
[0,1,2,3,4].
but then the 4 and the 2 were swapped so that on the next iteration when the 
probe_index was modded by 4 it a value would be generated that is not 2 but 
still random among the remaining possibilities. The array that the result of this 
mod would be mapped onto is:
[0,1,4,3,2].

The previous section is the conceptual explanation of how n! probe sequences can 
be generated. In practice it takes a lot of space and time to generate arrays 
and swap values in them when you are just trying to create a probe sequence. For 
this reason, the code written does not directly follow the previous explanation 
but rather uses an integer encoding of the above ideas in order to achieve the 
same result. The general idea is that each index can have some "swap_adjustment" 
added onto it after it has been generated in order to get the correct unique 
index. For the example listed previously, this swap adjustment would look like:
[0,0,2,0,3]
because if the index of 2 is generated, then the adjustment of 2 can be added to 
it in order to get the swapped index of 4. Similarly if the index of 4 is 
generated then the adjustment of 3 can be added to it in order to get the 
swapped value of 2(4 + 3 wraps around to the index value of 2; (4 + 3) % 5 = 2).
Within this application, the last adjustment of 3 will never be used because 
of how each iteration the probe index is modded by a decreasing number, so the 
above array can also just be represented as: 
[0,0,2,0,0]
In order to save space this array can be encoded as an integer. Each value in 
the array can take on 5 different values because there are 5 different positions 
in the array so really this array is just the number 200 in base 5. As long as 
this number is carefully tracked and then adjusted for each swap it is not 
necessary to maintain an array to keep track of the swaps that have occurred.
This is how the n! probe sequence were generated within this project.

One final note: In order to read off the swaps from a value in base x, it can be
expensive to perform exponent operations to get the right value to div and 
modulus by. For that reason an array was maintained to access these values 
quickly at any time. When the initial array where the elements would be stored 
was constructed, a "size_powers" array was also constructed to allow for the 
size of the array raised to any power between 0-n to be easily found.
