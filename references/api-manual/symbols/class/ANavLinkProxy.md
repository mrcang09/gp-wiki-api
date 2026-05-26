# ANavLinkProxy

- Symbol Type: class
- Symbol Path: Others / ANavLinkProxy
- Source JSON Path: class/detail/Others/ANavLinkProxy.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/ANavLinkProxy.json
- Mirrored At (UTC): 2026-05-19 08:23:20Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointLinks | TArray < FNavigationLink > | Navigation links (point to point) added to navigation data |  |
| SegmentLinks | TArray < FNavigationSegmentLink > | Navigation links (segment to segment) added to navigation data<br>		@todo hidden from use until we fix segment links. Not really working now |  |
| SmartLinkComp | UNavLinkCustomComponent * | Smart link: can affect path following |  |
| bSmartLinkIsRelevant | bool | Smart link: toggle relevancy |  |
| EdRenderComp | UNavLinkRenderingComponent * | Editor Preview |  |
| SpriteComponent | UBillboardComponent * |  |  |

## Functions

### ReceiveSmartLinkReached

called when agent reaches smart link during path following, use ResumePathFollowing() to give control back

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Agent | AActor *  |  |  |
| Destination | FVector & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResumePathFollowing

resume normal path following

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Agent | AActor * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsSmartLinkEnabled

check if smart link is enabled

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetSmartLinkEnabled

change state of smart link

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HasMovingAgents

check if any agent is moving through smart link right now

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |
