# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> The above functions are all considered hash functions because they share key properties that define what 
> a hash function is. Each function takes in two parameters: a key (a string) and a size (an integer). The 
> key is the data that the hash function processes to produce a hash value, and the size represents the 
> maximum index value of the hash map or hash table, essentially defining the range of possible hash 
> values.
> 
> One main feature of these hash functions is that they are deterministic. This means that for a given 
> input key, the function will always produce the same hash value. Determinism is essential for reliability 
> in storing and retrieving data because it ensures that the same key consistently maps to the same index 
> in a hash table. This property is vital for data structures like dictionaries or hash maps, where 
> consistent key mapping allows for efficient data retrieval.
> 
> Another key feature is that they map arbitrary inputs to a fixed-size output. Regardless of the length 
> or content of the input key—be it a single character, a sentence, or an entire paragraph, the hash 
> function compresses it into an integer within a specific range determined by the size parameter. This 
> allows the hash function to handle inputs of varying lengths while producing outputs that fit within a 
> predefined range suitable for indexing in data structures.
> 
> The main differences between each function lie in their level of hashing complexity, uniformity, and the 
> distribution of hashed keys they produce. Some functions are simple and fast but may result in more 
> collisions (e.g., functions 1 and 2), while others are more complex and provide a better distribution 
> across the hash table to minimize collisions (e.g., functions 3, 4, and 5).
> 
> A key feature of a strong hashing algorithm, is its ability to minimise collisions and ensure a uniform 
> distribution of hash values. This means it should spread input keys evenly across the entire range 
> of possible outputs, reducing the likelihood that different keys produce the same hash value. Additionally, 
> other features of a strong hashing function are that it is computationally efficient 
> (without excessive resource consumption), and if security is a concern, such as in cryptographic 
> applications, hash functions should also be designed to be irreversible and collision-resistant.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> The advantages and disadvantages of each hash function is listed below for the examples provided:
> 
> 1. Stupidly Simple Hash (SSH):
> 
> Uniformity: 
> This function does hash keys to a value but all the keys are hashed to same value of 1 and are not unique.
> Since one of the main benefits and goals of hashing is to enable quick data access, the SSH function 
> wouldn’t be effective unless the algorithm was modified to distribute hashes across a hash table. Without 
> such modifications, SSH isn’t suitable for any real application.
> 
> Determinism:
> The given input will always produce the same output, however all inputs will produce the same answer.
> Efficiency: 
> The SSH is a very simple function that returns 1 in constant time.
> 
> Collision Resistance: 
> There are no mechanisms implemented to avoid collisions as all keys are hashed to the same value.
> Sensitivity to input changes: Any changes in the input will not produce any changes in the output.
> Security:
>     There is only one possible output for this hash function as it always produces 1. This means there is
>     no randomness or unpredictability making it very insecure.
> 
> 2. Sum of ASCII Values Hash Function
> 
> Uniformity: 
> This function sums the ASCII values of the characters in the key and then takes the modulus with the 
> table size. While it provides a better distribution than the SSH, it may still not distribute hash values 
> uniformly, especially if keys share common characters or lengths. This can lead to clustering of hash values.
> Determinism: Given a specific input key, this function will always produce the same output hash value. 
> Therefore, it is deterministic.
>
> Efficiency: 
> The time complexity is O(n), where n equals the length of the key, because it iterates over each character 
> in the key. This is efficient as long as the key isn't too large, and depending on the use case it may become 
> less optimal compared to constant-time hash functions.
> Sensitivity to input changes: Small changes in the input key (like changing a single character) may not 
> significantly change the output hash value, especially if the ASCII values of the characters are similar. 
> Therefore, it has low sensitivity to input changes.
> 
> Security:
> Non-Reversibility: 
> Due to the straightforward calculation of summing ASCII values, it is relatively easy to find an 
> input key that produces a specific hash value. If an attacker had a list of common passwords hashed values,
> they could compare the users value and possibly find a key that produces it. Alternatively, an attacker could 
> generate possible keys that sum up to the same total and test them.
> 
> Randomness and Unpredictability: 
> The output hash values are predictable and do not appear random, making it unsuitable for use cases where 
> security of data is of the utmost importance. 
> 
> 3. Pearson Hash Function
> 
> Uniformity:
> The Pearson hash function is designed to produce an even distribution of hash values across the hash table. 
> By using the XOR operation, this function compares the binary representations of integers which helps to 
> minimise clustering and spread hash values evenly.
> 
> Determinism: 
> This function is deterministic as long as the permutation table remains the same. This is why the
> pearson_hash function uses the random.seed(42), so that the pearson table remains the same every time the 
> code is run. Because of this, given the same input key and permutation table, it will always produce the 
> same hash value.
> 
> Efficiency: 
> The time complexity is O(n), where n is the length of the input key. It processes each character in the 
> key once, making it relatively efficient for keys that aren't too long.
> 
> Collision Resistance: 
> The Pearson hash function has good collision resistance for small datasets due to its design. 
> However, since it ultimately produces a hash value modulo the table size, collisions can still occur, especially 
> if the table size is small relative to the number of possible inputs.
> 
> Sensitivity to input changes: 
> The Pearson Hash function is highly sensitive to input changes, meaning even a small modification to the input 
> (such as changing a single character) will produce a very different hash value. The XOR operation and 
> shuffled permutation table contribute to this sensitivity and increases allow hash values to be spread out 
> more evenly across the hash table.
> 
> Security:
> Non-Reversibility: 
> While it's more secure than simpler hash functions, the Pearson hash is not cryptographically secure. If the 
> permutation table is known, it might be possible to reverse-engineer the input key, especially for shorter keys.
> Randomness and Unpredictability: 
> The shuffled permutation table adds an element of randomness, making the hash outputs less predictable. 
> However, if the permutation table is fixed or known (as in the provided code with a fixed random seed), 
> the outputs become predictable. For better security, the permutation table should be generated with true 
> randomness,which as discussed in class, is very challenging to do. By using random.shuffle(), it decreases 
> the odds of and attacker being able to reverse-engineer the function, which makes this more suitable for use 
> cases which aren't storing highly sensitive data.
> 
> 4. Built-in Hash Function
> 
> According to Python's in-built Hash documentation: https://docs.python.org/3/library/functions.html#hash, the 
> implementation of the hash function is different for different data types (e.g., integers, strings, tuples).
> It also handles hash collisions internally by probing for an open slot in the hash table to store the new item.
> 
> Uniformity:
> The built-in hash function in Python provides reasonably good uniformity in distributing hash values, though 
> it does depend on the underlying implementation used between different Python versions.
> 
> Determinism:
> The built-in hash is deterministic within the same Python session, which means the same input will consistently 
> produce the same hash value. However, further research shows that from Python version 3.3 and onwards:
> "The hash value is different when invoked a second time because recent releases of Python 
> (versions 3.3 and up), by default, apply a random hash seed for this function. The seed changes on each 
> invocation of Python." 
> https://kinsta.com/blog/python-hashing/#pythons-builtin-hashing-function
> 
> Efficiency:
> This function is very efficient, with an average time complexity of O(1), as it directly calls the 
> Python-internal hashing function.
> 
> Collision Resistance:
> The built-in hash function is optimised for minimal collisions, although it is still possible for collisions to 
> occur with large datasets. Python handles collisions internally by probing for an open slot in the hash table
> to store the new item.
> 
> Sensitivity to input changes: 
> Small changes in input result in a significant difference in the hash value. This makes the built-in hash 
> function sensitive to input changes.
> 
> Security:
> The in-build hash function is suitable for use cases which aren't storing highly sensitive data, but is not 
> considered cryptographically secure. From python versions 3.3+ however, this is a lot more secure given the 
> changes in random seed for each session, but hash values may be predictable if the session state is known. 
> 
> 5. SHA256 Hashing Function from Hashlib
> 
> SHA-256 (Secure Hash Algorithm) is part of the SHA-2 family of cryptographic hash functions:
> It takes an input (like a string) and processes it in blocks of 512 bits through multiple rounds of 
> calculations, mixing up and scrambling the data to produce a unique 256-bit hash value.
> https://en.wikipedia.org/wiki/SHA-2
> https://docs.python.org/3/library/hashlib.html#hashlib.sha3_256
> https://helix.stormhub.org/papers/SHA-256.pdf
> 
> Uniformity:
> SHA-256 produces a very uniform distribution of hash values. This means that when you hash different inputs, 
> they’re spread out across a large range, reducing collisions. This is due to the cryptographic properties of 
> the algorithm which aims to spread hash values across the full output range. 
> 
> Determinism:
> SHA-256 is deterministic, meaning that given the same input, it will always produce the same output hash value. 
> This consistency makes it reliable for use cases requiring verification and repeatability.
> 
> Efficiency:
> SHA-256 is less efficient than simpler hash functions like sum_of_ascii_values due to its cryptographic 
> complexity. It has a time complexity of O(n) with respect to the input size. The additional computation 
> is generally not an issue for short strings but may be a concern with very large datasets or real-time 
> applications. But for use cases with sensitive data this is an acceptable trade off.  
> 
> Collision Resistance:
> SHA-256 is highly resistant to collisions, meaning it’s extremely unlikely to find two different inputs that 
> produce the same hash value. This feature makes SHA-256 suitable for applications requiring data integrity, 
> such as digital signatures and secure file verification.
> 
> Sensitivity to Input Changes: 
> SHA-256 has a high sensitivity to input changes. A single-bit difference in the input will produce a 
> completely different hash output, even a small change in input is reflected drastically in the hash result.
> 
> Security: 
> SHA-256 is considered a secure cryptographic hash function, suitable when dealing with highly sensitive data.
> It provides non-reversibility, randomness (or very close to), and unpredictability in its output. It is 
> widely used in cryptographic applications such as password storage, data integrity verification, and 
> blockchain technology. 
> While the SHA-256 is secure for most applications, it is not immune to future advances in computing, 
> such as quantum computing. However, given the potential of quantum computing, and it's potential to solve 
> calculations exponentially faster than current technology, it is likely that new hashing technologies would
> be required to secure sensitive data.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> When thinking about the main use case of a hash-map, if I consider the main benefit being fast data retrieval, 
> I would list the three most important attributes in this order: 
> 
> Uniformity: 
> I would say this is the most crucial attribute because it directly impacts the overall performance of the 
> hash map. Poor uniformity leads to clustering, which causes more collisions and due to this slower 
> lookups and insertions. If you consider the SSH for example, when the distribution isn't uniform, the hash 
> map becomes inefficient, especially as the number of elements grows.
> 
> Determinism: 
> This is an essential aspect of Hashing for consistency in accessing the correct values. Determinism 
> guarantees that the same input key will always produce the same hash value. without determinism, we 
> couldn’t reliably look up keys in the hash map, and the hash function needs to consistently return the same 
> location for each key in order to retrieve, update, or delete data accurately. 
> 
> Efficiency:
> Efficiency is an important attribute but is not as critical as "Uniformity" and "Determinism", these enable 
> the functionality of the hash map first and efficiency enhances performance. If the hash function is slow or 
> complex, the performance advantage of using a hash map is reduced. Ideally, a hash function with a time 
> complexity of O(1) is ideal, as it keeps operations like lookups, inserts, and deletes at constant time. 
> For applications where speed is a priority, or for large datasets, an efficient hash function makes the 
> hash map a viable choice.

Dynamic and Flexible Structure: Unlike arrays that require contiguous memory, hash maps use buckets to store values, which makes them more flexible with memory allocation and efficient for dynamically growing datasets.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> For this task, I chose the Pearson Hash function to meet the requirements. The main reasons for this are that
> it has a good spread of hash values across the hash table, reducing collisions, it is deterministic and also 
> efficient. It was also essential that the function was sensitive to input changes, meaning a small change
> produced a completely different hash value. I considered using the SHA-256 hashing function for its strong 
> security properties, but for my use case with example player data, cryptographic security was not necessary
> and the Pearson Hashing function met the requirements. 

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> (3) Pearson hash function
> https://en.wikipedia.org/wiki/Pearson_hashing
> 
> import random
> 
> """Importing the random module allows the functionality of shuffling the permutation table and also the 
> ability to apply a random seed to the shuffle. This contributes to "Uniformity" by adding randomness to the 
> hash table, which makes the distribution of hash values spread more evenly.
> """
> 
> random.seed(42)
> 
> """This applies a fixed seed to the shuffling of the random number generator, which makes sure that every
> time the code runs, it produces the same shuffled Pearson table. By fixing the seed, it makes the function
> deterministic, meaning it will consistently return the same hash for a given input. 
> """
> 
> This is INCORRECT:
> pearson_table = [random.randint(0, 255) for _ in range(256)] 
> """During a lecture, this was pointed out to be incorrect as the permutation table should have a range of 
> integers from 0 to 255 and each integer should appear once. However, the above code produces random 
> integers 256 times, and the same integer could appear more than once causing duplicate values. 
> """
>
> pearson_table = list(range(256))
> """This creates a list of integers from 0 to 255 to form the Pearson table, which will be used to mix 
> and spread hash values. The table provides uniformity by allowing the hash function to map inputs across 
> a wide range.
> """
> 
> random.shuffle(pearson_table)
> """The Pearson table is then shuffled after it is created with integers from 0 to 255. This reduces the
> chances of clustering where similar inputs produce similar hash value. For example, given the input 
> "password" and "pa55word", the function should map to a different hash values even though they are similar, 
> by shuffling the permutation table it helps maintain uniformity. It also slightly increases security by
> adding an element of unpredictability. 
> """
> 
> def pearson_hash(key: str, size: int) -> int:
> """This defines the Pearson hash function, where it takes in a string key and the hash table size, and 
> returns an integer between 0 and size-1 as an index. This function provides uniformity and collision 
> resistance by spreading hash values across a well-defined range. The "size" will be used in the final step of
> the function in conjunction with the modulo operator to return an integer which will be used to map the hashed 
> key to a particular index. 
> """
>     hash_ = 0            # Initialises the hash variable to a value of 0. 
>     
>     for char in key: 
>     """Begins to loop over each character in the key (string). This contributes to sensitivity in input changes,
>        by allowing each character in the key to affect the hash value.
>     """
>        
>         hash_ = pearson_table[hash_ ^ ord(char)]
>         """This line is the core of the Pearson hashing process. For each character, it takes the XOR of 
>            hash_ with the ASCII (integer) value of the character (ord(char)) and then uses this as an index 
>            to get a new value from the pearson_table. This step contributes significantly to uniformity and 
>            collision resistance by scrambling the bits of the hash at each step. It also increases
>            sensitivity to input changes since even a minor change in input will change the final result 
>            due to XOR’s binary properties.
>         """
>
> return hash_ % size
> """ This line finalises the hash value by taking hash_ modulo the size. The size parameter is equal to the 
> bounds of the hash table, so this ensures that the returned result is within the available range of the hash 
> table (from 0 to size - 1). The modulo operation here supports uniformity by limiting the output range to fit 
> the table size which is essential to avoid indexing to out-of-bounds values.
> """
>
6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Pseudocode for Storing Players in a Hash Map
> 1. Initialise the Hash Map:

> Create a hash map (dictionary) where each key is an integer representing a hash value, and each value is 
> a PlayerList object (which will hold Player objects and their attributes). The hash map size (SIZE = constant) 
> which defines the range of possible hash values (initialise with 10 PlayerList objects).
> 
> 2. Create Hash Function (Pearson Hash):
>
> Define a pearson_hash function that takes a player’s UID as input.
> Use the Pearson hash algorithm to convert the UID into an integer value using each character and pythons "ord"
> operator.
> Use the modulo operation with the hash map SIZE to ensure the result fits within the hash map index range.
> 
> 3. Add or Update a Player:
> 
> Hash the player’s UID to determine the appropriate hash map index.
> Check if the hash map at this index already has a PlayerList.
> If not, create a new PlayerList at this index.
> Call add_or_update_player() on the PlayerList to:
> Add the player if they don’t already exist in the list.
> Update the player’s name if a player with the same UID already exists.
> 
> 4. Retrieve a Player by UID:
> 
> Hash the given UID to find the correct index in the hash map.
> Check if a PlayerList exists at this index.
> If it does, call get_player_by_uid() on the PlayerList to retrieve the player.
> If not, raise an error indicating the player was not found.
> 
> 5. Delete a Player by UID:
> 
> Hash the given UID to locate the correct index in the hash map.
> Check if a PlayerList exists at this index.
> If it does, call delete_player_by_uid() on the PlayerList to remove the player.
> If the list is empty after deletion, consider removing the PlayerList from the hash map.
> 
> 6. Display Players:
> 
> For each index in the hash map:
> If there’s a PlayerList at that index, call display() on it to print the players in order.
"""

## Reflection

1. What was the most challenging aspect of this task?

> For me there were two equally challenging aspects of this task. The first was comprehending the processes 
> involved behind hashing algorithms enough to be able to implement it within my own Player data structure. 
> Initially, I thought that I understood the theory behind this quite well, but this was put to the test 
> when having to implement this myself in my existing player data code. 
> 
> Secondly, during the implementation process, I found it took some time to fully understand the complexities 
> of having a Player object with its own set of attributes, also represented by a PlayerNode with links 
> to other nodes, then placed inside a PlayerList which is essentially a list of 10 lists (buckets) each 
> containing dictionaries where the index is the hashed value and the key is the PlayerNode. It felt like working 
> within layers of nested structures, and reminded me of the movie inception!

It was a benefit to  
> To help with understanding the relationships and layers, I drew out the data structure on a piece of paper. 
> This visual representation helped greatly in understanding the relationships between the elements and lists 
> more clearly and made it easier to understand how each part would interact in the code.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> If I didn’t have to use a PlayerList, I would have implemented the hash map as a simple list of lists 
> (buckets), where each index represents a hashed value. In this approach, each bucket would contain the 
> Player objects directly, and if a collision occurs (i.e., two players hash to the same bucket), they are 
> simply appended to the bucket list. This implementation is easier to understand and maintain but has 
> trade-offs. Searching within each bucket may be slower since we lose the doubly linked list’s quick 
> removals and ability to traverse in both directions. Removing or updating a specific player would require 
> iterating through the bucket to find the matching Player. However, this trade-off can still perform well 
> if the dataset is not too large.

## Reference
https://en.wikipedia.org/wiki/Pearson_hashing
https://docs.python.org/3/library/functions.html#hash
https://docs.python.org/3/library/hashlib.html
https://en.wikipedia.org/wiki/SHA-2
https://en.wikipedia.org/wiki/SHA-2#Pseudocode
https://kinsta.com/blog/python-hashing/#pythons-builtin-hashing-function
https://docs.python.org/3/library/hashlib.html#hashlib.sha3_256
https://helix.stormhub.org/papers/SHA-256.pdf

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
