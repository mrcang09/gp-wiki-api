# UTwitterIntegrationBase

- Symbol Type: class
- Symbol Path: Others / UTwitterIntegrationBase
- Source JSON Path: class/detail/Others/UTwitterIntegrationBase.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UTwitterIntegrationBase.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Functions

### Init

Perform any needed initialization

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### CanShowTweetUI

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the user is allowed to use the Tweet UI |  |

### ShowTweetUI

Kicks off a tweet, using the platform to show the UI. If this returns false, or you are on a platform that doesn't support the UI,
	  you can use the TwitterRequest method to perform a manual tweet using the Twitter API

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InitialMessage | FString &  | [optional] Initial message to show |  |
| URL | FString &  | [optional] URL to attach to the tweet |  |
| Picture | FString & | [optional] Name of a picture (stored locally, platform subclass will do the searching for it) to add to the tweet |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if a UI was displayed for the user to interact with, and a TID_TweetUIComplete will be sent |  |

### AuthorizeAccounts

Starts the process of authorizing the local user(s). When TID_AuthorizeComplete is called, then GetNumAccounts() 
	  will return a valid number of accounts

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the authorization process started, and TID_AuthorizeComplete delegates will be called |  |

### GetNumAccounts

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 | The number of accounts that were authorized |  |

### GetAccountName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| AccountIndex | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString  | the display name of the given Twitter account |  |

### TwitterRequest

Kicks off a generic twitter request

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| URL | FString &  | The URL for the twitter request |  |
| ParamKeysAndValues | TArray < FString > &  |  |  |
| RequestMethod | ETwitterRequestMethod  |  |  |
| AccountIndex | int32 | A user index if an account is needed, or -1 if an account isn't needed for the request |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true the request was sent off, and a TID_RequestComplete |  |
