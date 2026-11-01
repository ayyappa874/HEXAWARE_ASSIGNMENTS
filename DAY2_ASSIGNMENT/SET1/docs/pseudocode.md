# Pseudocode - E-Commerce Catalogue and Traffic Analysis (Day 2)

Style: FUNCTION ... END FUNCTION, assignment with `←`, RETURN, IF / FOR / WHILE blocks.

## Task 1 - Binary Search Tree

**INSERT A CATEGORY INTO THE BST**

```
FUNCTION insert(tree, key)
    IF tree.root = EMPTY THEN
        tree.root ← NEW NODE(key)
        RETURN
    END IF

    current ← tree.root
    LOOP
        IF key = current.key THEN
            RETURN                              // duplicates are ignored
        ELSE IF key < current.key THEN
            IF current.left = EMPTY THEN
                current.left ← NEW NODE(key)
                RETURN
            END IF
            current ← current.left
        ELSE
            IF current.right = EMPTY THEN
                current.right ← NEW NODE(key)
                RETURN
            END IF
            current ← current.right
        END IF
    END LOOP
END FUNCTION
```

**SEARCH**

```
FUNCTION search(tree, key)
    current ← tree.root
    WHILE current ≠ EMPTY
        IF key = current.key THEN
            RETURN FOUND
        ELSE IF key < current.key THEN
            current ← current.left
        ELSE
            current ← current.right
        END IF
    END WHILE
    RETURN NOT_FOUND
END FUNCTION
```

**THE THREE TRAVERSALS**

```
FUNCTION inorder(node)
    IF node = EMPTY THEN
        RETURN
    END IF
    inorder(node.left)
    VISIT node                // add node.key to the result
    inorder(node.right)
END FUNCTION

FUNCTION preorder(node)
    IF node = EMPTY THEN
        RETURN
    END IF
    VISIT node
    preorder(node.left)
    preorder(node.right)
END FUNCTION

FUNCTION postorder(node)
    IF node = EMPTY THEN
        RETURN
    END IF
    postorder(node.left)
    postorder(node.right)
    VISIT node
END FUNCTION
```

## Task 2 - Hash table with chaining

**HASH FUNCTION, PUT AND GET (CHAINING)**

```
FUNCTION hashIndex(key, capacity)
    h ← 0
    FOR EACH character IN key
        h ← (h × 31 + CODE(character)) MOD capacity
    END FOR
    RETURN h
END FUNCTION

FUNCTION put(table, key, value)
    chain ← table.buckets[hashIndex(key, table.capacity)]
    FOR EACH pair IN chain
        IF pair.key = key THEN
            pair.value ← value
            RETURN
        END IF
    END FOR

    APPEND (key, value) TO chain          // a collision just makes the chain longer
    table.size ← table.size + 1
    IF table.size / table.capacity > 0.75 THEN
        growTable(table)
    END IF
END FUNCTION

FUNCTION get(table, key)
    chain ← table.buckets[hashIndex(key, table.capacity)]
    FOR EACH pair IN chain
        IF pair.key = key THEN
            RETURN pair.value
        END IF
    END FOR
    RETURN NOT_FOUND
END FUNCTION
```

**GROWING THE TABLE WHEN IT GETS CROWDED**

```
FUNCTION growTable(table)
    old ← table.buckets
    table.capacity ← table.capacity × 2 + 1
    table.buckets ← NEW EMPTY BUCKETS(table.capacity)
    FOR EACH pair IN ALL CHAINS OF old
        APPEND pair TO table.buckets[hashIndex(pair.key, table.capacity)]
    END FOR
END FUNCTION
```

## Task 3 - Graph: deployment order

**DEPLOYMENT ORDER WITH DFS (also finds the circular dependency)**

```
FUNCTION deployOrderDFS(dependsOn)
    order ← EMPTY LIST
    state[every service] ← NOT_VISITED

    FOR EACH service IN all services
        IF state[service] = NOT_VISITED THEN
            cycle ← visit(service)
            IF cycle EXISTS THEN
                RETURN NO_ORDER, cycle
            END IF
        END IF
    END FOR

    RETURN order
END FUNCTION

FUNCTION visit(service)
    state[service] ← ON_CURRENT_PATH
    ADD service TO path

    FOR EACH dep IN dependsOn[service]
        IF state[dep] = ON_CURRENT_PATH THEN
            RETURN path FROM dep ONWARD, PLUS dep      // circular dependency
        ELSE IF state[dep] = NOT_VISITED THEN
            cycle ← visit(dep)
            IF cycle EXISTS THEN
                RETURN cycle
            END IF
        END IF
    END FOR

    REMOVE service FROM path
    state[service] ← FINISHED
    APPEND service TO order            // all its dependencies are already in the order
    RETURN NO_CYCLE
END FUNCTION
```

**DEPLOYMENT ORDER WITH BFS (queue of services that are ready)**

```
FUNCTION deployOrderBFS(dependsOn)
    FOR EACH service
        waiting[service] ← NUMBER OF dependencies of service
    END FOR

    queue ← all services WHERE waiting[service] = 0
    order ← EMPTY LIST

    WHILE queue IS NOT EMPTY
        service ← DEQUEUE(queue)
        APPEND service TO order
        FOR EACH other THAT DEPENDS ON service
            waiting[other] ← waiting[other] - 1
            IF waiting[other] = 0 THEN
                ENQUEUE other INTO queue
            END IF
        END FOR
    END WHILE

    IF LENGTH(order) < NUMBER OF services THEN
        RETURN NO_ORDER, services NOT IN order        // circular dependency
    END IF
    RETURN order
END FUNCTION
```

## Task 4 - Sliding window

**SLIDING WINDOW**

```
FUNCTION busiestWindow(counts, k)
    window ← SUM OF counts[0 .. k - 1]
    bestTotal ← window
    bestStart ← 0

    FOR i ← k TO LENGTH(counts) - 1
        window ← window + counts[i] - counts[i - k]    // add the new minute, drop the old one
        IF window > bestTotal THEN
            bestTotal ← window
            bestStart ← i - k + 1
        END IF
    END FOR

    RETURN bestStart, bestTotal
END FUNCTION
```

## Task 5 - Two pointers

**TWO POINTERS ON A SORTED LIST**

```
FUNCTION findPairs(values, target)
    left ← 0
    right ← LENGTH(values) - 1
    pairs ← EMPTY LIST

    WHILE left < right
        total ← values[left] + values[right]

        IF total = target THEN
            APPEND (values[left], values[right]) TO pairs
            a ← values[left]
            b ← values[right]
            WHILE left < right AND values[left] = a
                left ← left + 1
            END WHILE
            WHILE left < right AND values[right] = b
                right ← right - 1
            END WHILE
        ELSE IF total < target THEN
            left ← left + 1                // sum too small: need a bigger left value
        ELSE
            right ← right - 1              // sum too big: need a smaller right value
        END IF
    END WHILE

    RETURN pairs
END FUNCTION
```
