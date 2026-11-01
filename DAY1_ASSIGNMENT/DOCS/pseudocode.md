# Pseudocode - Retail Order Desk (Day 1)

Style: FUNCTION ... END FUNCTION, assignment with `←`, RETURN, IF / FOR / WHILE blocks.

## Task 1 - Searching

**LINEAR SEARCH**

```
FUNCTION linearSearch(orders, targetId)
    FOR i ← 0 TO LENGTH(orders) - 1
        IF orders[i].orderId = targetId THEN
            RETURN i
        END IF
    END FOR
    RETURN NOT_FOUND
END FUNCTION
```

**BINARY SEARCH  (orders must be sorted by orderId)**

```
FUNCTION binarySearch(sortedOrders, targetId)
    low ← 0
    high ← LENGTH(sortedOrders) - 1

    WHILE low ≤ high
        mid ← FLOOR((low + high) / 2)

        IF sortedOrders[mid].orderId = targetId THEN
            RETURN mid
        ELSE IF sortedOrders[mid].orderId < targetId THEN
            low ← mid + 1
        ELSE
            high ← mid - 1
        END IF
    END WHILE

    RETURN NOT_FOUND
END FUNCTION
```

## Task 2 - Sorting

**BUBBLE SORT (DESCENDING)**

```
FUNCTION bubbleSortDescending(orders)
    n ← LENGTH(orders)

    FOR pass ← 1 TO n - 1
        swapped ← FALSE
        FOR j ← 0 TO n - 1 - pass
            IF orders[j].amount < orders[j + 1].amount THEN
                SWAP orders[j], orders[j + 1]
                swapped ← TRUE
            END IF
        END FOR

        IF swapped = FALSE THEN
            BREAK
        END IF
    END FOR

    RETURN orders
END FUNCTION
```

**MERGE SORT (DESCENDING)**

```
FUNCTION mergeSortDescending(orders)
    IF LENGTH(orders) ≤ 1 THEN
        RETURN orders
    END IF

    mid ← FLOOR(LENGTH(orders) / 2)
    left ← mergeSortDescending(orders[0 : mid])
    right ← mergeSortDescending(orders[mid : END])

    RETURN merge(left, right)
END FUNCTION

FUNCTION merge(left, right)
    result ← EMPTY LIST
    i ← 0
    j ← 0

    WHILE i < LENGTH(left) AND j < LENGTH(right)
        IF left[i].amount ≥ right[j].amount THEN
            APPEND left[i] TO result
            i ← i + 1
        ELSE
            APPEND right[j] TO result
            j ← j + 1
        END IF
    END WHILE

    APPEND REMAINING ITEMS OF left AND right TO result
    RETURN result
END FUNCTION
```

## Task 3 - Duplicates by sorting (no hashing)

**SORT AND COMPARE NEIGHBOURS (NO HASHING)**

```
FUNCTION findDuplicates(orders)
    sortedOrders ← SORT orders BY (customerId, amount, MINUTE OF createdAt)
    groups ← EMPTY LIST
    current ← [sortedOrders[0]]

    FOR i ← 1 TO LENGTH(sortedOrders) - 1
        IF KEY(sortedOrders[i]) = KEY(sortedOrders[i - 1]) THEN
            APPEND sortedOrders[i] TO current
        ELSE
            IF LENGTH(current) ≥ 2 THEN
                APPEND current TO groups
            END IF
            current ← [sortedOrders[i]]
        END IF
    END FOR

    IF LENGTH(current) ≥ 2 THEN
        APPEND current TO groups
    END IF

    RETURN groups
END FUNCTION
```

## Task 4 - Stack and Queue

**STACK (LAST IN, FIRST OUT) - used for UNDO**

```
FUNCTION push(stack, value)
    node ← NEW NODE(value)
    node.next ← stack.top
    stack.top ← node
    stack.size ← stack.size + 1
END FUNCTION

FUNCTION pop(stack)
    IF stack.top = EMPTY THEN
        RETURN ERROR "stack is empty"
    END IF

    value ← stack.top.value
    stack.top ← stack.top.next
    stack.size ← stack.size - 1
    RETURN value
END FUNCTION
```

**QUEUE (FIRST IN, FIRST OUT) - used for DISPATCH**

```
FUNCTION enqueue(queue, value)
    node ← NEW NODE(value)
    IF queue.tail = EMPTY THEN
        queue.head ← node
    ELSE
        queue.tail.next ← node
    END IF
    queue.tail ← node
    queue.size ← queue.size + 1
END FUNCTION

FUNCTION dequeue(queue)
    IF queue.head = EMPTY THEN
        RETURN ERROR "queue is empty"
    END IF

    value ← queue.head.value
    queue.head ← queue.head.next
    IF queue.head = EMPTY THEN
        queue.tail ← EMPTY
    END IF
    queue.size ← queue.size - 1
    RETURN value
END FUNCTION
```

**UNDO LAST EDIT**

```
FUNCTION editOrder(order, field, newValue, undoStack)
    push(undoStack, (order, field, order[field]))     // remember the OLD value
    order[field] ← newValue
END FUNCTION

FUNCTION undoLastEdit(undoStack)
    IF undoStack IS EMPTY THEN
        RETURN NO_ACTION
    END IF

    (order, field, oldValue) ← pop(undoStack)
    order[field] ← oldValue
END FUNCTION
```

## Task 5 - Greedy and Dynamic Programming

**GREEDY CHANGE-MAKING**

```
FUNCTION greedyChange(amount, denominations)
    SORT denominations IN DESCENDING ORDER
    remaining ← amount
    selected ← EMPTY LIST

    FOR EACH coin IN denominations
        count ← FLOOR(remaining / coin)
        APPEND (coin, count) TO selected
        remaining ← remaining MOD coin
    END FOR

    IF remaining = 0 THEN
        RETURN selected
    ELSE
        RETURN NO_EXACT_CHANGE
    END IF
END FUNCTION
```

**DYNAMIC PROGRAMMING CHANGE-MAKING**

```
FUNCTION minimumChange(amount, denominations)
    best[0] ← 0
    FOR value ← 1 TO amount
        best[value] ← INFINITY
        FOR EACH coin IN denominations
            IF coin ≤ value AND best[value - coin] + 1 < best[value] THEN
                best[value] ← best[value - coin] + 1
                choice[value] ← coin
            END IF
        END FOR
    END FOR

    IF best[amount] = INFINITY THEN
        RETURN NO_EXACT_CHANGE
    END IF

    selected ← EMPTY LIST
    value ← amount
    WHILE value > 0
        APPEND choice[value] TO selected
        value ← value - choice[value]
    END WHILE

    RETURN selected
END FUNCTION
```
