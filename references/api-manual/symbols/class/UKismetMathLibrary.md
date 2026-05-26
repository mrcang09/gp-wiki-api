# UKismetMathLibrary

- Symbol Type: class
- Symbol Path: Others / UKismetMathLibrary
- Source JSON Path: class/detail/Others/UKismetMathLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UKismetMathLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:31Z

---

## Functions

### RandomBool

Returns a uniformly distributed random bool

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### RandomBoolWithWeight

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
	 		Weight = .6 return value = True 60% of the time

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Weight | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RandomBoolWithWeightFromStream

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
			Weight = .6 return value = True 60% of the time

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Weight | float  |  |  |
| RandomStream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Not_PreBool

Returns the logical complement of the Boolean value (NOT A)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_BoolBool

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_BoolBool

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BooleanAND

Returns the logical AND of two values (A AND B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BooleanNAND

Returns the logical NAND of two values (A AND B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BooleanOR

Returns the logical OR of two values (A OR B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BooleanXOR

Returns the logical eXclusive OR of two values (A XOR B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### BooleanNOR

Returns the logical Not OR of two values (A NOR B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | bool  |  |  |
| B | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Multiply_ByteByte

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "Byte  Byte", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Byte")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Divide_ByteByte

Division (A  B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Percent_ByteByte

Modulo (A % B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Add_ByteByte

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Subtract_ByteByte

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### BMin

Returns the minimum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### BMax

Returns the maximum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Less_ByteByte

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_ByteByte

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_ByteByte

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_ByteByte

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_ByteByte

Returns true if A is equal to B (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_ByteByte

Returns true if A is not equal to B (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint8  |  |  |
| B | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Multiply_IntInt

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer  integer", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Divide_IntInt

Division (A  B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Percent_IntInt

Modulo (A % B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Add_IntInt

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Subtract_IntInt

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Less_IntInt

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_IntInt

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_IntInt

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_IntInt

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_IntInt

Returns true if A is equal to B (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_IntInt

Returns true if A is not equal to B (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### InRange_IntInt

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int32  |  |  |
| Min | int32  |  |  |
| Max | int32  |  |  |
| InclusiveMin | bool  |  |  |
| InclusiveMax | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### And_IntInt

Bitwise AND (A & B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Xor_IntInt

Bitwise XOR (A ^ B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Or_IntInt

Bitwise OR (A | B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Not_Int

Bitwise NOT (~A)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### LeftShift_Int

Bitwise LeftShift (A << N)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| N | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RightShift_Int

Bitwise RightShift (A >> N)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| N | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### LeftShift_Int64

Bitwise LeftShift (A << N)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| N | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### RightShift_Int64

Bitwise RightShift (A >> N)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| N | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### SignOfInteger

Sign (integer, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RandomInteger

Returns a uniformly distributed random number between 0 and Max - 1

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RandomIntegerInRange

Return a random integer between Min and Max (>= Min and <= Max)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | int32  |  |  |
| Max | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Min

Returns the minimum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Max

Returns the maximum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Clamp

Returns Value clamped to be between A and B (inclusive)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | int32  |  |  |
| A | int32  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Abs_Int

Returns the absolute (positive) value of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Multiply_Int64Int64

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer64  integer64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer64")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Divide_Int64Int64

Division (A  B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Add_Int64Int64

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Subtract_Int64Int64

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Less_Int64Int64

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_Int64Int64

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_Int64Int64

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_Int64Int64

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_Int64Int64

Returns true if A is equal to B (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_Int64Int64

Returns true if A is not equal to B (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### InRange_Int64Int64

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | int64  |  |  |
| Min | int64  |  |  |
| Max | int64  |  |  |
| InclusiveMin | bool  |  |  |
| InclusiveMax | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### And_Int64Int64

Bitwise AND (A & B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Xor_Int64Int64

Bitwise XOR (A ^ B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Or_Int64Int64

Bitwise OR (A | B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Not_Int64

Bitwise NOT (~A)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### SignOfInteger64

Sign (integer64, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### RandomInteger64

Returns a uniformly distributed random number between 0 and Max - 1

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### RandomInteger64InRange

Return a random integer64 between Min and Max (>= Min and <= Max)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | int64  |  |  |
| Max | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### MinInt64

Returns the minimum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### MaxInt64

Returns the maximum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### ClampInt64

Returns Value clamped to be between A and B (inclusive)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | int64  |  |  |
| A | int64  |  |  |
| B | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Abs_Int64

Returns the absolute (positive) value of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Multiply_UInt64UInt64

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta = (DisplayName = "uinteger64  uinteger64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Integer64")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Divide_UInt64UInt64

Division (A  B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Add_UInt64UInt64

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Subtract_UInt64UInt64

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Less_UInt64UInt64

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_UInt64UInt64

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_UInt64UInt64

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_UInt64UInt64

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_UInt64UInt64

Returns true if A is equal to B (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_UInt64UInt64

Returns true if A is not equal to B (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### InRange_UInt64UInt64

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | uint64  |  |  |
| Min | uint64  |  |  |
| Max | uint64  |  |  |
| InclusiveMin | bool  |  |  |
| InclusiveMax | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### And_UInt64UInt64

Bitwise AND (A & B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Xor_UInt64UInt64

Bitwise XOR (A ^ B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Or_UInt64UInt64

Bitwise OR (A | B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### Not_UInt64

Bitwise NOT (~A)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### RandomUInteger64

Returns a uniformly distributed random number between 0 and Max - 1

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### RandomUInteger64InRange

Return a random integer64 between Min and Max (>= Min and <= Max)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | uint64  |  |  |
| Max | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### MinUInt64

Returns the minimum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### MaxUInt64

Returns the maximum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### ClampUInt64

Returns Value clamped to be between A and B (inclusive)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | uint64  |  |  |
| A | uint64  |  |  |
| B | uint64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint64  |  |  |

### MultiplyMultiply_FloatFloat

Power (Base to the Exp-th power)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Base | float  |  |  |
| Exp | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Multiply_FloatFloat

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "float  float", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Float")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Multiply_IntFloat

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "int  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Float")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Divide_FloatFloat

Division (A  B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Percent_FloatFloat

Modulo (A % B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Fraction

Returns the fractional part of a float.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Add_FloatFloat

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Subtract_FloatFloat

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Less_FloatFloat

Returns true if A is Less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_FloatFloat

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_FloatFloat

Returns true if A is Less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_FloatFloat

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_FloatFloat

Returns true if A is exactly equal to B (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NearlyEqual_FloatFloat

Returns true if A is nearly equal to B (|A - B| < ErrorTolerance)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_FloatFloat

Returns true if A does not equal B (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### InRange_FloatFloat

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| Min | float  |  |  |
| Max | float  |  |  |
| InclusiveMin | bool  |  |  |
| InclusiveMax | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Hypotenuse

Returns the hypotenuse of a right-angled triangle given the width and height.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Width | float  |  |  |
| Height | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GridSnap_Float

Snaps a value to the nearest grid multiple. E.g.,
	 		Location = 5.1, GridSize = 10.0 : return value = 10.0
	  If GridSize is 0 Location is returned
	  if GridSize is very small precision issues may occur.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Location | float  |  |  |
| GridSize | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Abs

Returns the absolute (positive) value of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Sin

Returns the sine of A (expects Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Asin

Returns the inverse sine (arcsin) of A (result is in Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Cos

Returns the cosine of A (expects Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Acos

Returns the inverse cosine (arccos) of A (result is in Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Tan

Returns the tan of A (expects Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Atan

Returns the inverse tan (atan) (result is in Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Atan2

Returns the inverse tan (atan2) of AB (result is in Radians)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Exp

Returns exponential(e) to the power A (e^A)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Log

Returns log of A base B (if B^R == A, returns R)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| Base | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Loge

Returns natural log of A (if e^R == A, returns R)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Sqrt

Returns square root of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Square

Returns square of A (AA)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### RandomFloat

Returns a random float between 0 and 1

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### RandomFloatInRange

Generate a random number between Min and Max

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | float  |  |  |
| Max | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetPI

Returns the value of PI

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### GetTAU

Returns the value of TAU (= 2  PI)

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### DegreesToRadians

Returns radians value based on the input degrees

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### RadiansToDegrees

Returns degrees value based on the input radians

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegSin

Returns the sin of A (expects Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegAsin

Returns the inverse sin (arcsin) of A (result is in Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegCos

Returns the cos of A (expects Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegAcos

Returns the inverse cos (arccos) of A (result is in Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegTan

Returns the tan of A (expects Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegAtan

Returns the inverse tan (atan) (result is in Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### DegAtan2

Returns the inverse tan (atan2) of AB (result is in Degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### ClampAngle

Clamps an arbitrary angle to be between the given angles.  Will clamp to nearest boundary.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AngleDegrees | float  |  |  |
| MinAngleDegrees | float  | "from" angle that defines the beginning of the range of valid angles (sweeping clockwise) |  |
| MaxAngleDegrees | float | "to" angle that defines the end of the range of valid angles |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | Returns clamped angle in the range -180..180. |  |

### FMin

Returns the minimum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FMax

Returns the maximum value of A and B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FClamp

Returns Value clamped between A and B (inclusive)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | float  |  |  |
| A | float  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### MaxOfIntArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IntArray | TArray < int32 > &  |  |  |
| IndexOfMaxValue | int32 &  |  |  |
| MaxValue | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MinOfIntArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IntArray | TArray < int32 > &  |  |  |
| IndexOfMinValue | int32 &  |  |  |
| MinValue | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MaxOfFloatArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FloatArray | TArray < float > &  |  |  |
| IndexOfMaxValue | int32 &  |  |  |
| MaxValue | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MinOfFloatArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FloatArray | TArray < float > &  |  |  |
| IndexOfMinValue | int32 &  |  |  |
| MinValue | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MaxOfByteArray

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ByteArray | TArray < uint8 > &  |  |  |
| IndexOfMaxValue | int32 &  |  |  |
| MaxValue | uint8 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MinOfByteArray

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ByteArray | TArray < uint8 > &  |  |  |
| IndexOfMinValue | int32 &  |  |  |
| MinValue | uint8 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Lerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float  |  |  |
| V | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### InverseLerp

Returns the fraction (alpha) of the range B-A that corresponds to Value, e.g.,
		inputs A = 0, B = 8, Value = 3 : outputs Return Value = 38, indicating Value is 38 from A to B 
		inputs A = 8, B = 0, Value = 3 : outputs Return Value = 58, indicating Value is 58 from A to B
	 Named InverseLerp because Lerp( A, B, InverseLerp(A, B, Value) ) == Value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  | The "from" value this float could be, usually but not necessarily a minimum. Returned as 0. |  |
| B | float  | The "to" value this float could be, usually but not necessarily a maximum. Returned as 1. |  |
| Value | float | A value intended to be normalized relative to B-A |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | A normalized alpha value considering A and B. |  |

### Ease

Easeing  between A and B using a specified easing function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float  |  |  |
| Alpha | float  |  |  |
| EasingFunc | TEnumAsByte < EEasingFunc :: Type >  |  |  |
| BlendExp | float  |  |  |
| Steps | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Round

Rounds A to the nearest integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### FFloor

Rounds A to the largest previous integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### FTrunc

Rounds A to an integer with truncation towards zero.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### FTruncVector

Rounds A to an integer with truncation towards zero for each element in a vector.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVector | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntVector  |  |  |

### FCeil

Rounds A to the smallest following integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### FMod

Returns the number of times Divisor will go into Dividend (i.e., Dividend divided by Divisor), as well as the remainder

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Dividend | float  |  |  |
| Divisor | float  |  |  |
| Remainder | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### SignOfFloat

Sign (float, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### NormalizeToRange

Returns Value normalized to the given range.  (e.g. 20 normalized to the range 10->50 would result in 0.25)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| RangeMin | float  |  |  |
| RangeMax | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### MapRangeUnclamped

Returns Value mapped from one range into another.  (e.g. 20 normalized from the range 10->50 to 20->40 would result in 25)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| InRangeA | float  |  |  |
| InRangeB | float  |  |  |
| OutRangeA | float  |  |  |
| OutRangeB | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### MapRangeClamped

Returns Value mapped from one range into another where the Value is clamped to the Input Range.  (e.g. 0.5 normalized from the range 0->1 to 0->50 would result in 25)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float  |  |  |
| InRangeA | float  |  |  |
| InRangeB | float  |  |  |
| OutRangeA | float  |  |  |
| OutRangeB | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### MultiplyByPi

Multiplies the input value by pi. 
	UFUNCTION(BlueprintPure, meta=(Keywords = " multiply"), Category="Math|Float")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FInterpEaseInOut

Interpolate between A and B, applying an ease inout function.  Exp controls the degree of the curve.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float  |  |  |
| Alpha | float  |  |  |
| Exponent | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### MakePulsatingValue

Simple function to create a pulsating scalar value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCurrentTime | float  | Current absolute time |  |
| InPulsesPerSecond | float  | How many full pulses per second? |  |
| InPhase | float | Optional phase amount, between 0.0 and 1.0 (to synchronize pulses) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  Pulsating value (0.0-1.0) |  |

### FixedTurn

Returns a new rotation component value

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCurrent | float  | is the current rotation value |  |
| InDesired | float  | is the desired rotation value |  |
| InDeltaRate | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | a new rotation component value clamped in the range (-360,360) |  |

### Multiply_VectorFloat

Scales Vector A by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Multiply_VectorInt

Scales Vector A by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  int", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Multiply_VectorVector

UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  vector", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Vector")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Divide_VectorFloat

Vector divide by a float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Divide_VectorInt

Vector divide by an integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Divide_VectorVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Add_VectorVector

Vector addition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Add_VectorFloat

Adds a float to each component of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Add_VectorInt

Adds an integer to each component of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Subtract_VectorVector

Vector subtraction

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Subtract_VectorFloat

Subtracts a float from each component of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Subtract_VectorInt

Subtracts an integer from each component of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### LessLess_VectorRotator

Returns result of vector A rotated by the inverse of Rotator B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GreaterGreater_VectorRotator

Returns result of vector A rotated by Rotator B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RotateAngleAxis

Returns result of vector A rotated by AngleDeg around Axis

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVect | FVector  |  |  |
| AngleDeg | float  |  |  |
| Axis | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### EqualEqual_VectorVector

Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_VectorVector

Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Dot_VectorVector

Returns the dot product of two 3d vectors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Cross_VectorVector

Returns the cross product of two 3d vectors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### DotProduct2D

Returns the dot product of two 2d vectors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### CrossProduct2D

Returns the cross product of two 2d vectors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### VSize

Returns the length of the FVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### VSize2D

Returns the length of a 2d FVector.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### VSizeSquared

Returns the squared length of the FVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### VSize2DSquared

Returns the squared length of a 2d FVector.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Normal

Returns a unit normal version of the FVector A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Normal2D

Returns a unit normal version of the vector2d A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### VLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector  |  |  |
| V | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### VEase

Easeing  between A and B using a specified easing function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector  |  |  |
| Alpha | float  |  |  |
| EasingFunc | TEnumAsByte < EEasingFunc :: Type >  |  |  |
| BlendExp | float  |  |  |
| Steps | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### VContainsNan

Returns true if the vector contains NAN

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RandomUnitVector

Returns a random vector with length of 1

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector |  |  |

### RandomPointInBoundingBox

Returns a random point within the specified bounding box

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Origin | FVector &  |  |  |
| BoxExtent | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInConeInRadians

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector  |   The base "center" direction of the cone. |  |
| ConeHalfAngleInRadians | float | The half-angle of the cone (from ConeDir to edge), in radians. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInConeInDegrees

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector  |   The base "center" direction of the cone. |  |
| ConeHalfAngleInDegrees | float | The half-angle of the cone (from ConeDir to edge), in degrees. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInEllipticalConeInRadians

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector  |  |  |
| MaxYawInRadians | float  | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |  |
| MaxPitchInRadians | float | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInEllipticalConeInDegrees

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector  |  |  |
| MaxYawInDegrees | float  | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |  |
| MaxPitchInDegrees | float | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### MirrorVectorByNormal

Mirrors a vector by a normal

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### ProjectVectorOnToVector

Projects one vector (V) onto another (Target) and returns the projected vector.
	 If Target is nearly zero in length, returns the zero vector.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | FVector  | Vector to project. |  |
| Target | FVector | Vector on which we are projecting. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | V projected on to Target. |  |

### GetReflectionVector

Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
	  Produces a result like shining a laser at a mirror!

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Direction | FVector  | Direction vector the ray is coming from. |  |
| SurfaceNormal | FVector | A normal of the surface the ray should be reflected on. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  Reflected vector. |  |

### FindNearestPointsOnLineSegments

Find closest points between 2 segments.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Segment1Start | FVector  | Start of the 1st segment. |  |
| Segment1End | FVector  | End of the 1st segment. |  |
| Segment2Start | FVector  | Start of the 2nd segment. |  |
| Segment2End | FVector  | End of the 2nd segment. |  |
| Segment1Point | FVector &  | Closest point on segment 1 to segment 2. |  |
| Segment2Point | FVector & | Closest point on segment 2 to segment 1. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### FindClosestPointOnSegment

Find the closest point on a segment to a given point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point for which we find the closest point on the segment. |  |
| SegmentStart | FVector  | Start of the segment. |  |
| SegmentEnd | FVector | End of the segment. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | The closest point on the segment to the given point. |  |

### FindClosestPointOnLine

Find the closest point on an infinite line to a given point.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point for which we find the closest point on the line. |  |
| LineOrigin | FVector  | Point of reference on the line. |  |
| LineDirection | FVector | Direction of the line. Not required to be normalized. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | The closest point on the line to the given point. |  |

### GetPointDistanceToSegment

Find the distance from a point to the closest point on a segment.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point for which we find the distance to the closest point on the segment. |  |
| SegmentStart | FVector  | Start of the segment. |  |
| SegmentEnd | FVector | End of the segment. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The distance from the given point to the closest point on the segment. |  |

### GetPointDistanceToLine

Find the distance from a point to the closest point on an infinite line.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point for which we find the distance to the closest point on the line. |  |
| LineOrigin | FVector  | Point of reference on the line. |  |
| LineDirection | FVector | Direction of the line. Not required to be normalized. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The distance from the given point to the closest point on the line. |  |

### ProjectPointOnToPlane

Projects a point onto a plane defined by a point on the plane and a plane normal.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  | Point to project onto the plane. |  |
| PlaneBase | FVector  | A point on the plane. |  |
| PlaneNormal | FVector | Normal of the plane. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | Point projected onto the plane. |  |

### ProjectVectorOnToPlane

Projects a vector onto a plane defined by a normalized vector (PlaneNormal).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| V | FVector  | Vector to project onto the plane. |  |
| PlaneNormal | FVector | Normal of the plane. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | Vector projected onto the plane. |  |

### NegateVector

Negate a vector.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### ClampVectorSize

Clamp the vector size between a min and max length

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| Min | float  |  |  |
| Max | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetMinElement

Find the minimum element (X, Y or Z) of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetMaxElement

Find the maximum element (X, Y or Z) of a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetVectorArrayAverage

Find the average of an array of vectors

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Vectors | TArray < FVector > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetDirectionUnitVector

Find the unit direction vector from one position to another.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| From | FVector  |  |  |
| To | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### EqualEqual_RotatorRotator

Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_RotatorRotator

Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Multiply_RotatorFloat

Returns rotator representing rotator A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### Multiply_RotatorInt

Returns rotator representing rotator A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator (int)", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### ComposeRotators

Combine 2 rotations to give you the resulting rotation of first applying A, then B.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### NegateRotator

Negate a rotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### NormalRotator

Negate a rotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### GetAxes

Get the reference frame direction vectors (axes) described by this rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| X | FVector &  |  |  |
| Y | FVector &  |  |  |
| Z | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RandomRotator

Generates a random rotation, with optional random roll.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bRoll | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### RLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator  |  |  |
| Alpha | float  |  |  |
| bShortestPath | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### REase

Easeing  between A and B using a specified easing function

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator  |  |  |
| Alpha | float  |  |  |
| bShortestPath | bool  |  |  |
| EasingFunc | TEnumAsByte < EEasingFunc :: Type >  |  |  |
| BlendExp | float  |  |  |
| Steps | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### RContainsNan

Returns true if the rotation contains NAN

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NormalizedDeltaRotator

Normalized A-B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### RotatorFromAxisAndAngle

Create a rotation from an axis and and angle (in degrees)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Axis | FVector  |  |  |
| Angle | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### ClampAxis

Clamps an angle to the range of [0, 360].

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Angle | float | The angle to clamp. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The clamped angle. |  |

### NormalizeAxis

Clamps an angle to the range of [-180, 180].

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Angle | float | The Angle to clamp. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | The clamped angle. |  |

### LinearColorLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FLinearColor  |  |  |
| B | FLinearColor  |  |  |
| Alpha | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### LinearColorLerpUsingHSV

Linearly interpolates between two colors by the specified Alpha amount (100% of A when Alpha=0 and 100% of B when Alpha=1).  The interpolation is performed in HSV color space taking the shortest path to the new color's hue.  This can give better results than a normal lerp, but is much more expensive.  The incoming colors are in RGB space, and the output color will be RGB.  The alpha value will also be interpolated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FLinearColor  | The color and alpha to interpolate from as linear RGBA |  |
| B | FLinearColor  | The color and alpha to interpolate to as linear RGBA |  |
| Alpha | float | Scalar interpolation amount (usually between 0.0 and 1.0 inclusive) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  | The interpolated color in linear RGB space along with the interpolated alpha value |  |

### Multiply_LinearColorLinearColor

Element-wise multiplication of two linear colors (RR, GG, BB, AA) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  (LinearColor)", CompactNodeTitle = ""), Category="Math|Color")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FLinearColor  |  |  |
| B | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### Multiply_LinearColorFloat

Element-wise multiplication of a linear color by a float (FR, FG, FB, FA) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  Float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Color")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FLinearColor  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### MakePlaneFromPointAndNormal

Creates a plane with a facing direction of Normal at the given Point

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  | A point on the plane |  |
| Normal | FVector | The Normal of the plane at Point |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FPlane  | Plane instance |  |

### MakeDateTime

Makes a DateTime struct

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Year | int32  |  |  |
| Month | int32  |  |  |
| Day | int32  |  |  |
| Hour | int32  |  |  |
| Minute | int32  |  |  |
| Second | int32  |  |  |
| Millisecond | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime  |  |  |

### MakeDateTimeFromString

Makes a DateTime struct

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InString | FString & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime  |  |  |

### BreakDateTime

Breaks a DateTime into its components

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDateTime | FDateTime  |  |  |
| Year | int32 &  |  |  |
| Month | int32 &  |  |  |
| Day | int32 &  |  |  |
| Hour | int32 &  |  |  |
| Minute | int32 &  |  |  |
| Second | int32 &  |  |  |
| Millisecond | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Add_DateTimeTimespan

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime  |  |  |

### Subtract_DateTimeTimespan

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime  |  |  |

### Subtract_DateTimeDateTime

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### EqualEqual_DateTimeDateTime

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_DateTimeDateTime

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_DateTimeDateTime

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_DateTimeDateTime

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Less_DateTimeDateTime

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_DateTimeDateTime

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime  |  |  |
| B | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetDate

Returns the date component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime  |  |  |

### GetDay

Returns the day component of A (1 to 31)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetDayOfYear

Returns the day of year of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetHour

Returns the hour component of A (24h format)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetHour12

Returns the hour component of A (12h format)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMillisecond

Returns the millisecond component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMinute

Returns the minute component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMonth

Returns the month component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetSecond

Returns the second component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetTimeOfDay

Returns the time elapsed since midnight of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### GetYear

Returns the year component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### IsAfternoon

Returns whether A's time is in the afternoon

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsMorning

Returns whether A's time is in the morning

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FDateTime |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### DaysInMonth

Returns the number of days in the given year and month

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Year | int32  |  |  |
| Month | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### DaysInYear

Returns the number of days in the given year

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Year | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### IsLeapYear

Returns whether given year is a leap year

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Year | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### DateTimeMaxValue

Returns the maximum date and time value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime |  |  |

### DateTimeMinValue

Returns the minimum date and time value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime |  |  |

### Now

Returns the local date and time on this computer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime |  |  |

### Today

Returns the local date on this computer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime |  |  |

### UtcNow

Returns the UTC date and time on this computer

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FDateTime |  |  |

### DateTimeFromIsoString

Converts a date string in ISO-8601 format to a DateTime object

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsoString | FString  |  |  |
| Result | FDateTime & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### DateTimeFromString

Converts a date string to a DateTime object

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| DateTimeString | FString  |  |  |
| Result | FDateTime & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### MakeTimespan

Makes a Timespan struct

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Days | int32  |  |  |
| Hours | int32  |  |  |
| Minutes | int32  |  |  |
| Seconds | int32  |  |  |
| Milliseconds | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### MakeTimespan2

Makes a Timespan struct

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Days | int32  |  |  |
| Hours | int32  |  |  |
| Minutes | int32  |  |  |
| Seconds | int32  |  |  |
| FractionNano | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### BreakTimespan

Breaks a Timespan into its components

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTimespan | FTimespan  |  |  |
| Days | int32 &  |  |  |
| Hours | int32 &  |  |  |
| Minutes | int32 &  |  |  |
| Seconds | int32 &  |  |  |
| Milliseconds | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BreakTimespan2

Breaks a Timespan into its components

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTimespan | FTimespan  |  |  |
| Days | int32 &  |  |  |
| Hours | int32 &  |  |  |
| Minutes | int32 &  |  |  |
| Seconds | int32 &  |  |  |
| FractionNano | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Add_TimespanTimespan

Addition (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### Subtract_TimespanTimespan

Subtraction (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### Multiply_TimespanFloat

Scalar multiplication (A  s) 
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" multiply"), Category="Math|Timespan")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| Scalar | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### Divide_TimespanFloat

Scalar division (A  s) 
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" divide"), Category="Math|Timespan")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| Scalar | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### EqualEqual_TimespanTimespan

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_TimespanTimespan

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Greater_TimespanTimespan

Returns true if A is greater than B (A > B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GreaterEqual_TimespanTimespan

Returns true if A is greater than or equal to B (A >= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Less_TimespanTimespan

Returns true if A is less than B (A < B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### LessEqual_TimespanTimespan

Returns true if A is less than or equal to B (A <= B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetDays

Returns the days component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetDuration

Returns the absolute value of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### GetHours

Returns the hours component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMilliseconds

Returns the milliseconds component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetMinutes

Returns the minutes component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetSeconds

Returns the seconds component of A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### GetTotalDays

Returns the total number of days in A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetTotalHours

Returns the total number of hours in A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetTotalMilliseconds

Returns the total number of milliseconds in A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetTotalMinutes

Returns the total number of minutes in A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### GetTotalSeconds

Returns the total number of seconds in A

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### FromDays

Returns a time span that represents the specified number of days

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Days | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### FromHours

Returns a time span that represents the specified number of hours

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Hours | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### FromMilliseconds

Returns a time span that represents the specified number of milliseconds

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Milliseconds | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### FromMinutes

Returns a time span that represents the specified number of minutes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Minutes | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### FromSeconds

Returns a time span that represents the specified number of seconds

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Seconds | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan  |  |  |

### TimespanMaxValue

Returns the maximum time span value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan |  |  |

### TimespanMinValue

Returns the minimum time span value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan |  |  |

### TimespanRatio

Returns the ratio between two time spans (A  B), handles zero values

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTimespan  |  |  |
| B | FTimespan |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### TimespanZeroValue

Returns a zero time span value

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTimespan |  |  |

### TimespanFromString

Converts a time span string to a Timespan object

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TimespanString | FString  |  |  |
| Result | FTimespan & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_ByteToFloat

Converts a byte to a float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InByte | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Conv_IntToFloat

Converts an integer to a float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Conv_IntToInt64

Converts an integer to a 64 bit integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int64  |  |  |

### Conv_Int64ToInt

Converts an 64 bit integer to a 32 bit integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int64 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Conv_IntToByte

Converts an integer to a byte (if the integer is too large, returns the low 8 bits)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Conv_IntToIntVector

Converts an integer to an IntVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FIntVector  |  |  |

### Conv_IntToBool

Converts a int to a bool

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InInt | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Conv_BoolToInt

Converts a bool to an int

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBool | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Conv_BoolToFloat

Converts a bool to a float (0.0f or 1.0f)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBool | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### Conv_BoolToByte

Converts a bool to a byte

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InBool | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | uint8  |  |  |

### Conv_ByteToInt

Converts a byte to an integer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InByte | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### Conv_VectorToLinearColor

Converts a vector to LinearColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### Conv_LinearColorToVector

Converts a LinearColor to a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLinearColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Conv_ColorToLinearColor

Converts a color to LinearColor

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### Conv_LinearColorToColor

Converts a LinearColor to a color

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InLinearColor | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FColor  |  |  |

### Conv_VectorToTransform

Convert a vector to a transform. Uses vector as location

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTranslation | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### Conv_VectorToVector2D

Convert a Vector to a Vector2D

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Conv_Vector2DToVector

Convert a Vector2D to a Vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec2D | FVector2D  |  |  |
| Z | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Conv_IntVectorToVector

Convert an IntVector to a vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InIntVector | FIntVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Conv_FloatToVector

Convert a float into a vector, where each element is that float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFloat | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### Conv_FloatToLinearColor

Convert a float into a LinearColor, where each element is that float

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFloat | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### MakeBox

Makes an FBox from Min and Max and sets IsValid to true

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | FVector  |  |  |
| Max | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FBox  |  |  |

### MakeBox2D

Makes an FBox2D from Min and Max and sets IsValid to true

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | FVector2D  |  |  |
| Max | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FBox2D  |  |  |

### MakeVector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | float  |  |  |
| Y | float  |  |  |
| Z | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### BreakVector

Breaks a vector apart into X, Y, Z

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector  |  |  |
| X | float &  |  |  |
| Y | float &  |  |  |
| Z | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeVector2D

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | float  |  |  |
| Y | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### BreakVector2D

Breaks a 2D vector apart into X, Y.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector2D  |  |  |
| X | float &  |  |  |
| Y | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetForwardVector

Rotate the world forward vector by the given rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetRightVector

Rotate the world right vector by the given rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetUpVector

Rotate the world up vector by the given rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### CreateVectorFromYawPitch

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Yaw | float  |  |  |
| Pitch | float  |  |  |
| Length | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### GetYawPitchFromVector

Breaks a vector apart into Yaw, Pitch rotation values given in degrees. (non-clamped)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector  |  |  |
| Yaw | float &  |  |  |
| Pitch | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAzimuthAndElevation

Breaks a direction vector apart into Azimuth (Yaw) and Elevation (Pitch) rotation values given in degrees. (non-clamped)
	 Relative to the provided reference frame (an Actor's WorldTransform for example)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InDirection | FVector  |  |  |
| ReferenceFrame | FTransform &  |  |  |
| Azimuth | float &  |  |  |
| Elevation | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeRotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Roll | float  |  |  |
| Pitch | float  |  |  |
| Yaw | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### FindLookAtRotation

Find a rotation for an object at Start location to point at Target location.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Start | FVector &  |  |  |
| Target | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromX

Builds a rotator given only a XAxis. Y and Z are unspecified but will be orthonormal. XAxis need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromY

Builds a rotation matrix given only a YAxis. X and Z are unspecified but will be orthonormal. YAxis need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Y | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromZ

Builds a rotation matrix given only a ZAxis. X and Y are unspecified but will be orthonormal. ZAxis need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Z | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromXY

Builds a matrix with given X and Y axes. X will remain fixed, Y may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | FVector &  |  |  |
| Y | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromXZ

Builds a matrix with given X and Z axes. X will remain fixed, Z may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| X | FVector &  |  |  |
| Z | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromYX

Builds a matrix with given Y and X axes. Y will remain fixed, X may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Y | FVector &  |  |  |
| X | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromYZ

Builds a matrix with given Y and Z axes. Y will remain fixed, Z may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Y | FVector &  |  |  |
| Z | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromZX

Builds a matrix with given Z and X axes. Z will remain fixed, X may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Z | FVector &  |  |  |
| X | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### MakeRotFromZY

Builds a matrix with given Z and Y axes. Z will remain fixed, Y may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Z | FVector &  |  |  |
| Y | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### BreakRotator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator  |  |  |
| Roll | float &  |  |  |
| Pitch | float &  |  |  |
| Yaw | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BreakRotIntoAxes

Breaks apart a rotator into its component axes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator &  |  |  |
| X | FVector &  |  |  |
| Y | FVector &  |  |  |
| Z | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeTransform

Make a transform from location, rotation and scale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Translation | FVector  |  |  |
| Rotation | FRotator  |  |  |
| Scale | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### BreakTransform

Breaks apart a transform into location, rotation and scale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTransform | FTransform &  |  |  |
| Translation | FVector &  |  |  |
| Rotation | FRotator &  |  |  |
| Scale | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeRandomStream

Makes a SRand-based random number generator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InitialSeed | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRandomStream  |  |  |

### BreakRandomStream

Breaks apart a random number generator

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRandomStream | FRandomStream &  |  |  |
| InitialSeed | int32 & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeColor

Make a color from individual color components (RGB space)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| R | float  |  |  |
| G | float  |  |  |
| B | float  |  |  |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### BreakColor

Breaks apart a color into individual RGB components (as well as alpha)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor  |  |  |
| R | float &  |  |  |
| G | float &  |  |  |
| B | float &  |  |  |
| A | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HSVToRGB

Make a color from individual color components (HSV space)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| H | float  |  |  |
| S | float  |  |  |
| V | float  |  |  |
| A | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### RGBToHSV

Breaks apart a color into individual HSV components (as well as alpha)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColor | FLinearColor  |  |  |
| H | float &  |  |  |
| S | float &  |  |  |
| V | float &  |  |  |
| A | float & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HSVToRGB_Vector

Converts a HSV linear color (where H is in R, S is in G, and V is in B) to RGB

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HSV | FLinearColor  |  |  |
| RGB | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RGBToHSV_Vector

Converts a RGB linear color to HSV (where H is in R, S is in G, and V is in B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RGB | FLinearColor  |  |  |
| HSV | FLinearColor & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HexToRGB_Vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| HexString | FString  |  |  |
| bSRGB | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### RGB_VectorToHex

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| RGB | FLinearColor  |  |  |
| bSRGB | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### SelectString

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FString &  |  |  |
| B | FString &  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### SelectInt

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | int32  |  |  |
| B | int32  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### SelectFloat

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | float  |  |  |
| B | float  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### SelectVector

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector  |  |  |
| B | FVector  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### SelectRotator

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FRotator  |  |  |
| B | FRotator  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### SelectColor

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FLinearColor  |  |  |
| B | FLinearColor  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  |  |  |

### SelectTransform

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform &  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### SelectObject

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UObject *  |  |  |
| B | UObject *  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### SelectClass

If bPickA is true, A is returned, otherwise B is

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UClass *  |  |  |
| B | UClass *  |  |  |
| bSelectA | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UClass *  |  |  |

### MakeRotationFromAxes

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Forward | FVector  |  |  |
| Right | FVector  |  |  |
| Up | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### Conv_VectorToRotator

Create a rotator which orients X along the supplied direction vector

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVec | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### Conv_RotatorToVector

Get the X direction vector after this rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InRot | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### EqualEqual_ObjectObject

Returns true if A and B are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UObject *  |  |  |
| B | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_ObjectObject

Returns true if A and B are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UObject *  |  |  |
| B | UObject * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### EqualEqual_ClassClass

Returns true if A and B are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UClass *  |  |  |
| B | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_ClassClass

Returns true if A and B are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | UClass *  |  |  |
| B | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ClassIsChildOf

Determine if a class is a child of another class.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TestClass | TSubclassOf < UObject >  |  |  |
| ParentClass | TSubclassOf < UObject > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if TestClass == ParentClass, or if TestClass is a child of ParentClass; false otherwise, or if either |  |

### EqualEqual_NameName

Returns true if A and B are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FName  |  |  |
| B | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_NameName

Returns true if A and B are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FName  |  |  |
| B | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### TransformLocation

Transform a position by the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from local space to world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Location | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### TransformDirection

Transform a direction vector by the supplied transform - will not change its length. 
	 	For example, if T was an object's transform, this would transform a direction from local space to world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Direction | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### TransformRotation

Transform a rotator by the supplied transform. 
	 	For example, if T was an object's transform, this would transform a rotation from local space to world space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Rotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### InverseTransformLocation

Transform a position by the inverse of the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from world space to local space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Location | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### InverseTransformDirection

Transform a direction vector by the inverse of the supplied transform - will not change its length.
	 	For example, if T was an object's transform, this would transform a direction from world space to local space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Direction | FVector |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### InverseTransformRotation

Transform a rotator by the inverse of the supplied transform. 
	 	For example, if T was an object's transform, this would transform a rotation from world space to local space.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform &  |  |  |
| Rotation | FRotator |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### ComposeTransforms

Compose two transforms in order: A  B.
	 
	  Order matters when composing transforms:
	  A  B will yield a transform that logically first applies A then B to any subsequent transformation.
	 
	  Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
	  Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  | New transform: A  B |  |

### ConvertTransformToRelative

Returns the given transform, converted to be relative to the given ParentTransform.
	 
	  Example: AToB = ConvertTransformToRelative(AToWorld, BToWorld) to compute A relative to B.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Transform | FTransform &  | The transform you wish to convert |  |
| ParentTransform | FTransform & | The transform the conversion is relative to (in the same space as Transform) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  | 	The new relative transform |  |

### InvertTransform

Returns the inverse of the given transform T.
	  
	  Example: Given a LocalToWorld transform, WorldToLocal will be returned.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| T | FTransform & | The transform you wish to invert |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  | The inverse of T. |  |

### TLerp

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1).

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform &  |  |  |
| Alpha | float  |  |  |
| InterpMode | TEnumAsByte < ELerpInterpolationMode :: Type > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### TEase

Ease between A and B using a specified easing function.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform &  |  |  |
| Alpha | float  |  |  |
| EasingFunc | TEnumAsByte < EEasingFunc :: Type >  |  |  |
| BlendExp | float  |  |  |
| Steps | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### TInterpTo

Tries to reach a target transform.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FTransform &  |  |  |
| Target | FTransform &  |  |  |
| DeltaTime | float  |  |  |
| InterpSpeed | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FTransform  |  |  |

### EqualEqual_TransformTransform

Returns true if transform A is equal to transform B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NearlyEqual_TransformTransform

Returns true if transform A is nearly equal to B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FTransform &  |  |  |
| B | FTransform &  |  |  |
| LocationTolerance | float  | How close position of transforms need to be to be considered equal |  |
| RotationTolerance | float  | How close rotations of transforms need to be to be considered equal |  |
| Scale3DTolerance | float | How close scale of transforms need to be to be considered equal |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### Add_Vector2DVector2D

Returns addition of Vector A and Vector B (A + B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Subtract_Vector2DVector2D

Returns subtraction of Vector B from Vector A (A - B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Multiply_Vector2DFloat

Returns Vector A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector2d  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector2D")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Multiply_Vector2DVector2D

UFUNCTION(BlueprintPure, meta = (DisplayName = "vector2d  vector2d", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Vector2D")

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Divide_Vector2DFloat

Returns Vector A divided by B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Divide_Vector2DVector2D

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Add_Vector2DFloat

Returns Vector A added by B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### Subtract_Vector2DFloat

Returns Vector A subtracted by B

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  |  |  |

### EqualEqual_Vector2DVector2D

Returns true if vector2D A is equal to vector2D B (A == B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_Vector2DVector2D

Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FVector2D  |  |  |
| B | FVector2D  |  |  |
| ErrorTolerance | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### FInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | float  |  Actual position |  |
| Target | float  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 	New interpolated position |  |

### FInterpTo_Constant

Tries to reach Target at a constant rate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | float  |  Actual position |  |
| Target | float  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | 	New interpolated position |  |

### VInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FVector  |  Actual position |  |
| Target | FVector  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | 	New interpolated position |  |

### VInterpTo_Constant

Tries to reach Target at a constant rate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FVector  |  Actual position |  |
| Target | FVector  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  | 	New interpolated position |  |

### Vector2DInterpTo

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FVector2D  |  Actual position |  |
| Target | FVector2D  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  | 	New interpolated position |  |

### Vector2DInterpTo_Constant

Tries to reach Target at a constant rate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FVector2D  |  Actual position |  |
| Target | FVector2D  |  Target position |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D  | 	New interpolated position |  |

### RInterpTo

Tries to reach Target rotation based on Current rotation, giving a nice smooth feeling when rotating to Target rotation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FRotator  |  Actual rotation |  |
| Target | FRotator  |  Target rotation |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  | 	New interpolated position |  |

### RInterpTo_Constant

Tries to reach Target rotation at a constant rate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FRotator  |  Actual rotation |  |
| Target | FRotator  |  Target rotation |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  | 	New interpolated position |  |

### CInterpTo

Interpolates towards a varying target color smoothly.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FLinearColor  |  Current Color |  |
| Target | FLinearColor  |  Target Color |  |
| DeltaTime | float  | Time since last tick |  |
| InterpSpeed | float | Interpolation speed |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FLinearColor  | 	New interpolated Color |  |

### FloatSpringInterp

Uses a simple spring model to interpolate a float from Current to Target.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | float  |  Current value |  |
| Target | float  |  Target value |  |
| SpringState | FFloatSpringState &  |  Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |  |
| Stiffness | float  |  How stiff the spring model is (more stiffness means more oscillation around the target value) |  |
| CriticalDampingFactor | float  | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |  |
| DeltaTime | float  |  |  |
| Mass | float |   Multiplier that acts like mass on a spring |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### VectorSpringInterp

Uses a simple spring model to interpolate a vector from Current to Target.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Current | FVector  |  Current value |  |
| Target | FVector  |   Target value |  |
| SpringState | FVectorSpringState &  |  Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |  |
| Stiffness | float  |  How stiff the spring model is (more stiffness means more oscillation around the target value) |  |
| CriticalDampingFactor | float  | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |  |
| DeltaTime | float  |  |  |
| Mass | float |   Multiplier that acts like mass on a spring |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### ResetFloatSpringState

Resets the state of a given spring

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SpringState | FFloatSpringState & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetVectorSpringState

Resets the state of a given spring

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SpringState | FVectorSpringState & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RandomIntegerFromStream

Returns a uniformly distributed random number between 0 and Max - 1

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Max | int32  |  |  |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RandomIntegerInRangeFromStream

Return a random integer between Min and Max (>= Min and <= Max)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | int32  |  |  |
| Max | int32  |  |  |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  |  |  |

### RandomBoolFromStream

Returns a random bool

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RandomFloatFromStream

Returns a random float between 0 and 1

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### RandomFloatInRangeFromStream

Generate a random number between Min and Max

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Min | float  |  |  |
| Max | float  |  |  |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  |  |  |

### RandomUnitVectorFromStream

Returns a random vector with length of 1.0

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomRotatorFromStream

Create a random rotation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bRoll | bool  |  |  |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FRotator  |  |  |

### ResetRandomStream

Reset a random stream

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SeedRandomStream

Create a new random seed for a random stream

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRandomStreamSeed

Set the seed of a random stream to a specific number

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Stream | FRandomStream &  |  |  |
| NewSeed | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RandomUnitVectorInConeInRadiansFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector &  |   The base "center" direction of the cone. |  |
| ConeHalfAngleInRadians | float  | The half-angle of the cone (from ConeDir to edge), in radians. |  |
| Stream | FRandomStream & |   The random stream from which to obtain the vector. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInConeInDegreesFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector &  |   The base "center" direction of the cone. |  |
| ConeHalfAngleInDegrees | float  | The half-angle of the cone (from ConeDir to edge), in degrees. |  |
| Stream | FRandomStream & |   The random stream from which to obtain the vector. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInEllipticalConeInRadiansFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector &  |  |  |
| MaxYawInRadians | float  | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |  |
| MaxPitchInRadians | float  | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |  |
| Stream | FRandomStream & |  The random stream from which to obtain the vector. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### RandomUnitVectorInEllipticalConeInDegreesFromStream

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ConeDir | FVector &  |  |  |
| MaxYawInDegrees | float  | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |  |
| MaxPitchInDegrees | float  | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |  |
| Stream | FRandomStream & |  The random stream from which to obtain the vector. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector  |  |  |

### MinimumAreaRectangle

Finds the minimum area rectangle that encloses all of the points in InVerts

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| InVerts | TArray < FVector > &  | - Points to enclose in the rectangle |  |
| SampleSurfaceNormal | FVector &  |  |  |
| OutRectCenter | FVector &  |  |  |
| OutRectRotation | FRotator &  |  |  |
| OutSideLengthX | float &  |  |  |
| OutSideLengthY | float &  |  |  |
| bDebugDraw | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PointsAreCoplanar

Determines whether a given set of points are coplanar, with a tolerance. Any three points or less are always coplanar.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Points | TArray < FVector > &  | - The set of points to determine coplanarity for. |  |
| Tolerance | float | - Larger numbers means more variance is allowed. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the points are relatively coplanar, based on the tolerance |  |

### IsPointInBox

Determines whether the given point is in a box. Includes points on the box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point to test |  |
| BoxOrigin | FVector  | Origin of the box |  |
| BoxExtent | FVector | Extents of the box (distance in each axis from origin) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the point is in the box. |  |

### IsPointInBoxWithTransform

Determines whether a given point is in a box with a given transform. Includes points on the box.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Point | FVector  |  Point to test |  |
| BoxWorldTransform | FTransform &  | Component-to-World transform of the box. |  |
| BoxExtent | FVector |  Extents of the box (distance in each axis from origin), in component space. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | Whether the point is in the box. |  |

### LinePlaneIntersection

Computes the intersection point between a line and a plane.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LineStart | FVector &  |  |  |
| LineEnd | FVector &  |  |  |
| APlane | FPlane &  |  |  |
| T | float &  | - The t of the intersection between the line and the plane |  |
| Intersection | FVector & | - The point of intersection between the line and the plane |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 	True if the intersection test was successful. |  |

### LinePlaneIntersection_OriginNormal

Computes the intersection point between a line and a plane.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LineStart | FVector &  |  |  |
| LineEnd | FVector &  |  |  |
| PlaneOrigin | FVector  |  |  |
| PlaneNormal | FVector  |  |  |
| T | float &  | - The t of the intersection between the line and the plane |  |
| Intersection | FVector & | - The point of intersection between the line and the plane |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 	True if the intersection test was successful. |  |
