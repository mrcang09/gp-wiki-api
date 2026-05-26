# UBlueprintGameplayTagLibrary

- Symbol Type: class
- Symbol Path: Others / UBlueprintGameplayTagLibrary
- Source JSON Path: class/detail/Others/UBlueprintGameplayTagLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintGameplayTagLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:24Z

---

## Functions

### MatchesTag

Determine if TagOne matches against TagTwo

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagOne | FGameplayTag  |  Tag to check for match |  |
| TagTwo | FGameplayTag  |  Tag to check match against |  |
| bExactMatch | bool | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if TagOne matches TagTwo |  |

### MatchesAnyTags

Determine if TagOne matches against any tag in OtherContainer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagOne | FGameplayTag  |  Tag to check for match |  |
| OtherContainer | FGameplayTagContainer &  | Container to check against. |  |
| bExactMatch | bool | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | GAMEPLAYTAGS_API bool  | True if TagOne matches any tags explicitly present in OtherContainer |  |

### EqualEqual_GameplayTag

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTag  |  |  |
| B | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_GameplayTag

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTag  |  |  |
| B | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### IsGameplayTagValid

Returns true if the passed in gameplay tag is non-null

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTag | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetTagName

Returns FName of this tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTag | FGameplayTag & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FName  |  |  |

### MakeLiteralGameplayTag

Creates a literal FGameplayTag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTag  |  |  |

### GetNumGameplayTagsInContainer

Get the number of gameplay tags in the specified container

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer & | Tag container to get the number of tags from |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32  | The number of tags in the specified container |  |

### HasTag

Check if the tag container has the specified tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  Container to check for the tag |  |
| Tag | FGameplayTag  |   Tag to check for in the container |  |
| bExactMatch | bool |  If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the container has the specified tag, false if it does not |  |

### HasAnyTags

Check if the specified tag container has ANY of the tags in the other container

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  Container to check if it matches any of the tags in the other container |  |
| OtherContainer | FGameplayTagContainer &  | Container to check against. |  |
| bExactMatch | bool |  If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the container has ANY of the tags in the other container |  |

### HasAllTags

Check if the specified tag container has ALL of the tags in the other container

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  Container to check if it matches all of the tags in the other container |  |
| OtherContainer | FGameplayTagContainer &  | Container to check against. If this is empty, the check will succeed |  |
| bExactMatch | bool |  If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the container has ALL of the tags in the other container |  |

### DoesContainerMatchTagQuery

Check if the specified tag container matches the given Tag Query

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  Container to check if it matches all of the tags in the other container |  |
| TagQuery | FGameplayTagQuery & |  Query to match against |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the container matches the query, false otherwise. |  |

### GetAllActorsOfClassMatchingTagQuery

Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| ActorClass | TSubclassOf < AActor >  |  Class of actors to fetch |  |
| GameplayTagQuery | FGameplayTagQuery &  | Query to match against |  |
| OutActors | TArray < AActor * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddGameplayTag

Adds a single tag to the passed in tag container

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  |  |
| Tag | FGameplayTag |   The tag to add to the container |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RemoveGameplayTag

Remove a single tag from the passed in tag container, returns true if found

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer &  |  |  |
| Tag | FGameplayTag |   The tag to add to the container |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### AppendGameplayTagContainers

Appends all tags in the InTagContainer to InOutTagContainer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOutTagContainer | FGameplayTagContainer &  | The container that will be appended too. |  |
| InTagContainer | FGameplayTagContainer & | The container to append. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### EqualEqual_GameplayTagContainer

Returns true if the values are equal (A == B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTagContainer &  |  |  |
| B | FGameplayTagContainer & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_GameplayTagContainer

Returns true if the values are not equal (A != B)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTagContainer &  |  |  |
| B | FGameplayTagContainer & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### MakeLiteralGameplayTagContainer

Creates a literal FGameplayTagContainer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Value | FGameplayTagContainer |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer  |  |  |

### MakeGameplayTagContainerFromArray

Creates a FGameplayTagContainer from the array of passed in tags

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTags | TArray < FGameplayTag > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer  |  |  |

### MakeGameplayTagContainerFromTag

Creates a FGameplayTagContainer containing a single tag

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SingleTag | FGameplayTag |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagContainer  |  |  |

### BreakGameplayTagContainer

Breaks tag container into explicit array of tags

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTagContainer | FGameplayTagContainer &  |  |  |
| GameplayTags | TArray < FGameplayTag > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### MakeGameplayTagQuery

Creates a literal FGameplayTagQuery

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagQuery | FGameplayTagQuery | value to set the FGameplayTagQuery to |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FGameplayTagQuery  | The literal FGameplayTagQuery |  |

### HasAllMatchingGameplayTags

Check Gameplay tags in the interface has all of the specified tags in the tag container (expands to include parents of asset tags)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainerInterface | TScriptInterface < IGameplayTagAssetInterface >  | An Interface to a tag container |  |
| OtherContainer | FGameplayTagContainer & |  A Tag Container |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the tagcontainer in the interface has all the tags inside the container. |  |

### DoesTagAssetInterfaceHaveTag

Check if the specified tag container has the specified tag, using the specified tag matching types

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainerInterface | TScriptInterface < IGameplayTagAssetInterface >  | An Interface to a tag container |  |
| Tag | FGameplayTag |   Tag to check for in the container |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the container has the specified tag, false if it does not |  |

### NotEqual_TagTag

Checks if a gameplay tag's name and a string are not equal to one another

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTag  |  |  |
| B | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### NotEqual_TagContainerTagContainer

Checks if a gameplay tag containers's name and a string are not equal to one another

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| A | FGameplayTagContainer  |  |  |
| B | FString |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### GetDebugStringFromGameplayTagContainer

Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| TagContainer | FGameplayTagContainer & | The tag container to get the debug string from. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |

### GetDebugStringFromGameplayTag

Returns an FString representation of a gameplay tag for debugging purposes.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| GameplayTag | FGameplayTag | The tag to get the debug string from. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  |  |  |
