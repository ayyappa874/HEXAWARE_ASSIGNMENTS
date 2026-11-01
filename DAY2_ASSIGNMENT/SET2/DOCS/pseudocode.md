# Set 2 - Pseudocode

## Task 1 - BST

**INSERT INTO BST**

```
FUNCTION bstInsert(root, key)
  IF root = NULL THEN
    RETURN NEW NODE(key)
  END IF
  cur ← root
  WHILE TRUE
    IF key = cur.key THEN
      RETURN root                 // duplicate claim ID, ignore
    ELSE IF key < cur.key THEN
      IF cur.left = NULL THEN
        cur.left ← NEW NODE(key)
        RETURN root
      END IF
      cur ← cur.left
    ELSE
      IF cur.right = NULL THEN
        cur.right ← NEW NODE(key)
        RETURN root
      END IF
      cur ← cur.right
    END IF
  END WHILE
END FUNCTION
```

**SEARCH IN BST**

```
FUNCTION bstSearch(root, key)
  cur ← root
  steps ← 0
  WHILE cur ≠ NULL
    steps ← steps + 1
    IF key = cur.key THEN
      RETURN FOUND, steps
    ELSE IF key < cur.key THEN
      cur ← cur.left
    ELSE
      cur ← cur.right
    END IF
  END WHILE
  RETURN NOT_FOUND, steps
END FUNCTION
```

**THE THREE TRAVERSALS (shown recursively for clarity)**

```
FUNCTION inorder(node)        // LEFT, NODE, RIGHT  -> sorted order
  IF node = NULL THEN RETURN
  inorder(node.left)
  VISIT node
  inorder(node.right)
END FUNCTION

FUNCTION preorder(node)       // NODE, LEFT, RIGHT
  IF node = NULL THEN RETURN
  VISIT node
  preorder(node.left)
  preorder(node.right)
END FUNCTION

FUNCTION postorder(node)      // LEFT, RIGHT, NODE
  IF node = NULL THEN RETURN
  postorder(node.left)
  postorder(node.right)
  VISIT node
END FUNCTION
```

## Task 2 - Hashing

**NORMALISE AND GROUP CLAIMS**

```
FUNCTION normalise(policyNo, incidentDate)
  policy ← REMOVE ALL SPACES FROM policyNo
  policy ← UPPERCASE(policy)
  RETURN (policy, TRIM(incidentDate))
END FUNCTION

FUNCTION findDuplicates(claims)
  table ← NEW HASH MAP
  FOR EACH c IN claims
    key ← normalise(c.policyNo, c.incidentDate)
    IF key NOT IN table THEN
      table[key] ← [c.claimId]
    ELSE
      APPEND c.claimId TO table[key]
    END IF
  END FOR
  result ← EMPTY LIST
  FOR EACH (key, group) IN table
    IF LENGTH(group) ≥ 2 THEN APPEND (key, SORT(group)) TO result
  END FOR
  RETURN SORT(result)
END FUNCTION
```

**HASH MAP WITH CHAINING (HOW COLLISIONS ARE HANDLED)**

```
FUNCTION put(map, key, value)
  i ← hash(key) MOD LENGTH(map.buckets)
  FOR EACH pair IN map.buckets[i]       // walk the chain
    IF pair.key = key THEN
      pair.value ← value
      RETURN
    END IF
  END FOR
  APPEND (key, value) TO map.buckets[i]  // collision: add to chain
  map.size ← map.size + 1
  IF map.size / LENGTH(map.buckets) > 0.75 THEN
    resize(map)                          // double buckets, re-insert all
  END IF
END FUNCTION

FUNCTION get(map, key)
  i ← hash(key) MOD LENGTH(map.buckets)
  FOR EACH pair IN map.buckets[i]
    IF pair.key = key THEN RETURN pair.value
  END FOR
  RETURN NOT_FOUND
END FUNCTION
```

## Task 3 - Stage graph

**BFS - FEWEST STAGES BETWEEN TWO STAGES**

```
FUNCTION bfsShortestPath(graph, start, goal)
  IF start = goal THEN RETURN [start], 0
  parent ← MAP {start: NULL}
  queue ← [start]
  WHILE queue IS NOT EMPTY
    u ← DEQUEUE(queue)
    FOR EACH v IN graph[u]
      IF v NOT IN parent THEN
        parent[v] ← u
        IF v = goal THEN
          path ← walk parent[] from goal back to start, reversed
          RETURN path, LENGTH(path) - 1
        END IF
        ENQUEUE(queue, v)
      END IF
    END FOR
  END WHILE
  RETURN NO_ROUTE
END FUNCTION
```

**DFS - DETECT A LOOP (3 COLOURS)**

```
FUNCTION findCycle(graph)
  FOR EACH stage IN graph: colour[stage] ← WHITE
  FOR EACH s IN graph
    IF colour[s] = WHITE THEN
      colour[s] ← GREY
      path ← [s]
      stack ← [(s, its neighbours)]
      WHILE stack IS NOT EMPTY
        (u, neighbours) ← TOP(stack)
        FOR EACH v IN neighbours (continuing where we left off)
          IF colour[v] = GREY THEN
            RETURN path FROM v TO END, THEN v      // loop found
          ELSE IF colour[v] = WHITE THEN
            colour[v] ← GREY
            APPEND v TO path
            PUSH (v, its neighbours) ON stack
            BREAK                                  // go deeper first
          END IF
        END FOR
        IF no new stage was pushed THEN
          colour[u] ← BLACK
          POP stack
          REMOVE last item of path
        END IF
      END WHILE
    END IF
  END FOR
  RETURN NO_LOOP
END FUNCTION
```

## Task 4 - Sliding window

**SLIDING WINDOW - LONGEST RUN ABOVE A LIMIT**

```
FUNCTION longestRunAbove(counts, limit)
  bestLen ← 0
  bestStart ← -1
  left ← 0
  FOR right ← 0 TO LENGTH(counts) - 1
    IF counts[right] ≤ limit THEN
      left ← right + 1                 // window broken, restart after it
    ELSE IF right - left + 1 > bestLen THEN
      bestLen ← right - left + 1
      bestStart ← left
    END IF
  END FOR
  RETURN bestStart, bestLen
END FUNCTION
```

## Task 5 - Two-pointer merge

**MERGE TWO SORTED LISTS WITH TWO POINTERS**

```
FUNCTION mergeSorted(a, b)
  i ← 0
  j ← 0
  result ← EMPTY LIST
  WHILE i < LENGTH(a) AND j < LENGTH(b)
    IF a[i] ≤ b[j] THEN
      APPEND a[i] TO result
      i ← i + 1
    ELSE
      APPEND b[j] TO result
      j ← j + 1
    END IF
  END WHILE
  WHILE i < LENGTH(a)                  // leftover of a
    APPEND a[i] TO result
    i ← i + 1
  END WHILE
  WHILE j < LENGTH(b)                  // leftover of b
    APPEND b[j] TO result
    j ← j + 1
  END WHILE
  RETURN result
END FUNCTION
```

