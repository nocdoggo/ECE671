```bash
Name: Noctis Yamazaki Zhang
SPIRE ID: 34076138
```

## Homework #04

### **Problem 1 (25 Points): Prefix Matching**

1. Consider a datagram network using 8-bit host addresses. Suppose a router uses longest prefix matching and has the following forwarding table:

   

   | **Prefix Match** | **Interface** |
   | ---------------- | ------------- |
   | 0                | 0             |
   | 01               | 1             |
   | 000              | 2             |
   | otherwise        | 3             |


   For each of the four interfaces, give the associated range of destination host addresses and the number of addresses in the range.

2. Given the following forwarding table, create a binary tree that allows longest prefix match lookup.

   

   | **Interface** | **Prefix** |
   | ------------- | ---------- |
   | A             | 11/2       |
   | B             | 0101/4     |
   | C             | 011/3      |
   | D             | 01/2       |
   | E             | 0/1        |
   | F             | 0000/4     |

3. In that binary graph you created, show how a search for the appropriate interface for address 01001100 would be performed. Please indicate the individual steps in the correct order.

4. Create a tree in which always two bits per step are looked up (Trie).

5. 1. Show how a TCAM realization for the following forwarding table would look like.

      

   | **Interface** | **Prefix** |
   | ------------- | ---------- |
   | A             | 010**      |
   | B             | 0110*      |
   | C             | 011**      |
   | D             | 10011      |

**Problem 2 (25 Points): QUIC**