# Set 3 - Pseudocode

## Task 1 - BST

**INSERT INTO BST**

```
FUNCTION bstInsert(root, code)
  IF root = NULL THEN
    RETURN NEW NODE(code)
  END IF
  cur ← root
  WHILE TRUE
    IF code = cur.code THEN
      RETURN root                 // duplicate, ignore
    ELSE IF code < cur.code THEN
      IF cur.left = NULL THEN
        cur.left ← NEW NODE(code)
        RETURN root
      END IF
      cur ← cur.left
    ELSE
      IF cur.right = NULL THEN
        cur.right ← NEW NODE(code)
        RETURN root
      END IF
      cur ← cur.right
    END IF
  END WHILE
END FUNCTION
```

**SEARCH IN BST**

```
FUNCTION bstSearch(root, code)
  cur ← root
  steps ← 0
  WHILE cur ≠ NULL
    steps ← steps + 1
    IF code = cur.code THEN
      RETURN FOUND, steps
    ELSE IF code < cur.code THEN
      cur ← cur.left
    ELSE
      cur ← cur.right
    END IF
  END WHILE
  RETURN NOT_FOUND, steps
END FUNCTION
```

**HEIGHT OF BST (LEVEL BY LEVEL)**

```
FUNCTION bstHeight(root)
  IF root = NULL THEN
    RETURN 0
  END IF
  level ← [root]
  h ← 0
  WHILE level IS NOT EMPTY
    h ← h + 1
    next ← EMPTY LIST
    FOR EACH node IN level
      IF node.left ≠ NULL THEN APPEND node.left TO next
      IF node.right ≠ NULL THEN APPEND node.right TO next
    END FOR
    level ← next
  END WHILE
  RETURN h
END FUNCTION
```

## Task 2 - Hash map

**HASH MAP: PUT AND GET (CHAINING)**

```
FUNCTION put(map, key, value)
  i ← hash(key) MOD LENGTH(map.buckets)
  FOR EACH pair IN map.buckets[i]
    IF pair.key = key THEN
      pair.value ← value
      RETURN
    END IF
  END FOR
  APPEND (key, value) TO map.buckets[i]
  map.size ← map.size + 1
  IF map.size / LENGTH(map.buckets) > 0.75 THEN
    resize(map)                   // double buckets, re-insert all pairs
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

**FIND PARCELS SCANNED TWICE AT THE SAME HUB**

```
FUNCTION findDoubleScans(scans)
  counts ← NEW HASH MAP
  FOR EACH s IN scans
    key ← (s.trackingNo, s.hubCode, s.scannedAt)
    counts[key] ← counts.get(key, 0) + 1
  END FOR
  result ← EMPTY LIST
  FOR EACH (key, c) IN counts
    IF c > 1 THEN APPEND (key, c) TO result
  END FOR
  RETURN SORT(result)
END FUNCTION
```

## Task 3 - Graph

**BFS - FEWEST HOPS**

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

**DFS - ALL HUBS REACHABLE FROM THE DEPOT**

```
FUNCTION dfsReachable(graph, start)
  seen ← EMPTY SET
  order ← EMPTY LIST
  stack ← [start]
  WHILE stack IS NOT EMPTY
    u ← POP(stack)
    IF u IN seen THEN CONTINUE
    ADD u TO seen
    APPEND u TO order
    FOR EACH v IN REVERSE(graph[u])
      IF v NOT IN seen THEN PUSH(stack, v)
    END FOR
  END WHILE
  RETURN order
END FUNCTION
```

## Task 4 - Sliding window

**SLIDING WINDOW (HIGHEST k-HOUR AVERAGE)**

```
FUNCTION bestWindow(counts, k)
  IF LENGTH(counts) < k THEN RETURN NONE
  total ← SUM(counts[0 : k])
  bestSum ← total
  bestStart ← 0
  FOR i ← k TO LENGTH(counts) - 1
    total ← total + counts[i] - counts[i - k]
    IF total > bestSum THEN
      bestSum ← total
      bestStart ← i - k + 1
    END IF
  END FOR
  RETURN bestStart, bestSum / k
END FUNCTION
```

## Task 5 - Palindrome

**TWO-POINTER PALINDROME CHECK**

```
FUNCTION isPalindromeRoute(text)
  i ← 0
  j ← LENGTH(text) - 1
  WHILE i < j
    WHILE i < j AND text[i] IS NOT LETTER OR DIGIT
      i ← i + 1
    END WHILE
    WHILE i < j AND text[j] IS NOT LETTER OR DIGIT
      j ← j - 1
    END WHILE
    IF LOWER(text[i]) ≠ LOWER(text[j]) THEN
      RETURN FALSE
    END IF
    i ← i + 1
    j ← j - 1
  END WHILE
  RETURN TRUE
END FUNCTION
```

