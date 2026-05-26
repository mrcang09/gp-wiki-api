# UWidget

- Symbol Type: class
- Symbol Path: Others / UWidget
- Source JSON Path: class/detail/Others/UWidget.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidget.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Description

This is the base class for all wrapped Slate controls that are exposed to UObjects.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Slot | UPanelSlot * | The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget. |  |
| CachedPanel_ForGC | UPanelWidget * |  |  |
| ToolTipText | FText | Tooltip text to show when the user hovers over the widget with the mouse |  |
| ToolTipWidget | UWidget * | Tooltip widget to show when the user hovers over the widget with the mouse |  |
| IgnorePixelSnapping | bool |  |  |
| RelatedStyleWidgetName | FName |  |  |
| RelatedStyleWidget | TWeakObjectPtr < UWidget > |  |  |
| RenderTransform | FWidgetTransform | The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget. |  |
| RenderTransformPivot | FVector2D | The render transform pivot controls the location about which transforms are applied.<br>	  This value is a normalized coordinate about which things like rotations will occur. |  |
| bIsVariable | uint8 | Allows controls to be exposed as variables in a blueprint.  Not all controls need to be exposed<br>	  as variables, so this allows only the most useful ones to end up being exposed. |  |
| bCreatedByConstructionScript | uint8 | Flag if the Widget was created from a blueprint |  |
| bIsEnabled | uint8 | Sets whether this widget can be modified interactively by the user |  |
| bOverride_Cursor | uint8 |  |  |
| bIsVolatile | uint8 | Engine modify End<br>	<br>	<br>	  If true prevents the widget or its child's geometry or layout information from being cached.  If this widget<br>	  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile<br>	  instead of invalidating it every frame, which would prevent the invalidation panel from actually<br>	  ever caching anything. |  |
| bWriteSceneZBuffer | uint8 |  |  |
| UsedLayerPolicy | uint8 | DrawLayer's policy, 0: default, 1: prevent increasing layer to force batch |  |
| PreservedLayerNum | uint8 |  |  |
| FixedLayerPolicy | uint8 | DrawLayer's policy, 0: default, 1: Fixed layer to force batch |  |
| FixedLayerNum | uint8 |  |  |
| IngoreRectMove | uint8 |  |  |
| CareRectMove | uint8 |  |  |
| Cursor | TEnumAsByte < EMouseCursor :: Type > | The cursor to show when the mouse is over the widget |  |
| Clipping | EWidgetClipping | Controls how the clipping behavior of this widget.  Normally content that overflows the<br>	  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content<br>	  from being seen.<br>	 <br>	  NOTE: Elements in different clipping spaces can not be batched together, and so there is a<br>	  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent<br>	  content from showing up outside its bounds. |  |
| Visibility | ESlateVisibility | The visibility of the widget |  |
| RenderOpacity | float | The opacity of the widget |  |
| Navigation | UWidgetNavigation * | The navigation object for this widget is optionally created if the user has configured custom<br>	  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions<br>	  can occur between widgets. |  |
| bCatchVisibilityChangedEvent | bool | True if you want to enable auto destroy user widget stragegy |  |
| NativeBindings | TArray < UPropertyBinding * > | Native property bindings. |  |
| AreaTypeFlags | int32 |  |  |
| ZValue | int32 |  |  |
| bLogTraceVisibilityChange | uint8 | Engine modify Start |  |
| bHiddenInDesigner | uint8 | Stores the design time flag setting if the widget is hidden inside the designer |  |
| bExpandedInDesigner | uint8 | Stores the design time flag setting if the widget is expanded inside the designer |  |
| bLockedInDesigner | uint8 | Stores the design time flag setting if the widget is locked inside the designer |  |
| DesignerFlags | TEnumAsByte < EWidgetDesignFlags :: Type > | Any flags used by the designer at edit time. |  |
| DisplayLabel | FString | The friendly name for this widget displayed in the designer and BP graph. |  |
| bStyleHidding | bool |  |  |
| bStyleRemove | bool |  |  |
| bStyleInsertInvBox | bool |  |  |

## Functions

### SetRenderTransform

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InTransform | FWidgetTransform |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderScale

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Scale | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderShear

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Shear | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderAngle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Angle | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderTranslation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Translation | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetRenderTransformPivot

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Pivot | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetIsEnabled

Gets the current enabled status of the widget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetIsEnabled

Sets the current enabled status of the widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInIsEnabled | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetToolTipText

Sets the tooltip text for the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InToolTipText | FText & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetToolTip

Sets a custom widget as the tooltip of the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetCursor

Sets the cursor to show over the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InCursor | EMouseCursor :: Type |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ResetCursor

Resets the cursor to use on the widget, removing any customization for it.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsVisible

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible. |  |

### GetVisibility

Gets the current visibility of the widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESlateVisibility |  |  |

### GetUVisibility

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESlateVisibility |  |  |

### SetLocalVisibility

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldVisibility | ESlateVisibility  |  |  |
| NewVisibility | ESlateVisibility  |  |  |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetLocalVisibilityWithoutPCUIStyle

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OldVisibility | ESlateVisibility  |  |  |
| NewVisibility | ESlateVisibility  |  |  |
| Widget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetPCVisibility

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ESlateVisibility |  |  |

### IsPCVisible

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### SetVisibility

Sets the visibility of the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InVisibility | ESlateVisibility |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAdvancedCollapsed

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsAdvancedCollapsed | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetRenderOpacity

Gets the current visibility of the widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float |  |  |

### SetRenderOpacity

Sets the visibility of the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InOpacity | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetClipping

Gets the clipping state of this widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | EWidgetClipping |  |  |

### SetClipping

Sets the clipping state of this widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InClipping | EWidgetClipping |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ForceVolatile

Sets the forced volatility of the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bForce | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsVolatile

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsHovered

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the widget is currently being hovered by a pointer device |  |

### SetWriteSceneZBuffer

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bInWriteSceneZBuffer | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### HasKeyboardFocus

Checks to see if this widget currently has the keyboard focus

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  True if this widget has keyboard focus |  |

### HasMouseCapture

Checks to see if this widget is the current mouse captor

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  True if this widget has captured the mouse |  |

### SetKeyboardFocus

Sets the focus to this widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### HasUserFocus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if this widget is focused by a specific user. |  |

### HasAnyUserFocus

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if this widget is focused by any user. |  |

### HasFocusedDescendants

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if any descendant widget is focused by any user. |  |

### HasUserFocusedDescendants

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | true if any descendant widget is focused by a specific user. |  |

### SetUserFocus

Sets the focus to this widget for a specific user

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ForceLayoutPrepass

Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
	  One pre-pass is already happens for every widget before Tick occurs.  You only need to perform another
	  pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### InvalidateLayoutAndVolatility

Invalidates the widget from the view of a layout caching widget that may own this widget.
	  will force the owning widget to redraw and cache children on the next paint pass.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetDesiredSize

Gets the widgets desired size.
	  NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
	        have occurred before this value will be of any use.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D | The widget's desired size |  |

### SetAllNavigationRules

Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Rule | EUINavigationRule  | The rule to use when navigation is taking place |  |
| WidgetToFocus | FName | When using the Explicit rule, focus on this widget |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetNavigationRule

Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Direction | EUINavigation  |  |  |
| Rule | EUINavigationRule  | The rule to use when navigation is taking place |  |
| WidgetToFocus | FName | When using the Explicit rule, focus on this widget |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetParent

Gets the parent widget

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UPanelWidget * |  |  |

### RemoveFromParent

Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
	  it will also be removed from those containers.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetCachedGeometry

Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
	  the widget having been tickedpainted, or it may be out of date, or a frame behind.
	 
	  We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
	  try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
	  or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
	  being used to advise how to layout a dependent object the current frame.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const FGeometry & |  |  |

### GetCachedAllottedGeometry

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | const FGeometry & |  |  |

### SetIgnorePixelSnapping

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Ignore | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOwningPlayer

Gets the player controller associated with this UI.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APlayerController * | The player controller that owns the UI. |  |

### AddAdvancedCollapsedCount

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Num | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SubAdvancedCollapsedCount

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Num | uint8 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetWidgetOutlineName

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FString |  |  |

### IsCachedWidgetValid

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |
