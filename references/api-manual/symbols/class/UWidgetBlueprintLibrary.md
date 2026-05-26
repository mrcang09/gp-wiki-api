# UWidgetBlueprintLibrary

- Symbol Type: class
- Symbol Path: Others / UWidgetBlueprintLibrary
- Source JSON Path: class/detail/Others/UWidgetBlueprintLibrary.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UWidgetBlueprintLibrary.json
- Mirrored At (UTC): 2026-05-19 08:23:42Z

---

## Functions

### Create

Creates a widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| WidgetType | TSubclassOf < UUserWidget >  |  |  |
| OwningPlayer | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidget *  |  |  |

### CreateDragDropOperation

Creates a new drag and drop operation that can be returned from a drag begin to inform the UI what i
	  being dragged and dropped and what it looks like.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| OperationClass | TSubclassOf < UDragDropOperation > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UDragDropOperation *  |  |  |

### SetInputMode_UIOnly

Setup an input mode that allows only the UI to respond to user input.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APlayerController *  |  |  |
| InWidgetToFocus | UWidget *  |  |  |
| bLockMouseToViewport | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInputMode_UIOnlyEx

Setup an input mode that allows only the UI to respond to user input.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APlayerController *  |  |  |
| InWidgetToFocus | UWidget *  |  |  |
| InMouseLockMode | EMouseLockMode |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInputMode_GameAndUI

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APlayerController *  |  |  |
| InWidgetToFocus | UWidget *  |  |  |
| bLockMouseToViewport | bool  |  |  |
| bHideCursorDuringCapture | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInputMode_GameAndUIEx

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APlayerController *  |  |  |
| InWidgetToFocus | UWidget *  |  |  |
| InMouseLockMode | EMouseLockMode  |  |  |
| bHideCursorDuringCapture | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInputMode_GameOnly

Setup an input mode that allows only player input  player controller to respond to user input.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Target | APlayerController * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetFocusToGameViewport

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### DrawBox

Draws a box

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext &  |  |  |
| Position | FVector2D  |  |  |
| Size | FVector2D  |  |  |
| Brush | USlateBrushAsset *  |  |  |
| Tint | FLinearColor |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawLine

Draws a line.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext &  |  |  |
| PositionA | FVector2D  | Starting position of the line in local space. |  |
| PositionB | FVector2D  | Ending position of the line in local space. |  |
| Tint | FLinearColor  |  Color to render the line. |  |
| bAntiAlias | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawLines

Draws several line segments.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext &  |  |  |
| Points | TArray < FVector2D > &  | Line pairs, each line needs to be 2 separate points in the array. |  |
| Tint | FLinearColor  |  Color to render the line. |  |
| bAntiAlias | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawText

Draws text.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext &  |  |  |
| InString | FString &  | The string to draw. |  |
| Position | FVector2D  | The starting position where the text is drawn in local space. |  |
| Tint | FLinearColor |  Color to render the line. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### DrawTextFormatted

Draws text.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext &  |  |  |
| Text | FText &  |  The string to draw. |  |
| Position | FVector2D  | The starting position where the text is drawn in local space. |  |
| Font | UFont *  |  |  |
| FontSize | int32  |  |  |
| FontTypeFace | FName  |  |  |
| Tint | FLinearColor |  Color to render the line. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Handled

The event reply to use when you choose to handle an event.  This will prevent the event 
	  from continuing to bubble up  down the widget hierarchy.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply |  |  |

### Unhandled

The event reply to use when you choose not to handle an event.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply |  |  |

### CaptureMouse

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| CapturingWidget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### ReleaseMouseCapture

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### LockMouse

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| CapturingWidget | UWidget * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### UnlockMouse

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### SetUserFocus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| FocusWidget | UWidget *  |  |  |
| bInAllUsers | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### CaptureJoystick

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| CapturingWidget | UWidget *  |  |  |
| bInAllJoysticks | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### ClearUserFocus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| bInAllUsers | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### ReleaseJoystickCapture

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| bInAllJoysticks | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### SetMousePosition

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| NewMousePosition | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### DetectDrag

Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
	  and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply &  |  |  |
| WidgetDetectingDrag | UWidget *  | Detect dragging in this widget |  |
| DragKey | FKey |     This button should be pressed to detect the drag |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### DetectDragIfPressed

Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
	  If the DragKey is a touch key, that will also automatically work.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent &  | The pointer device event coming in. |  |
| WidgetDetectingDrag | UWidget *  | Detect dragging in this widget. |  |
| DragKey | FKey |     This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### EndDragDrop

An event should return FReply::Handled().EndDragDrop() to request that the current dragdrop operation be terminated.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Reply | FEventReply & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### IsDragDropping

Returns true if a dragdrop event is occurring that a widget can handle.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### GetDragDroppingContent

Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UDragDropOperation * |  |  |

### CancelDragDrop

Cancels any current drag drop operation.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### MakeBrushFromAsset

Creates a Slate Brush from a Slate Brush Asset

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| BrushAsset | USlateBrushAsset * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSlateBrush  | A new slate brush using the asset's brush. |  |

### MakeBrushFromTexture

Creates a Slate Brush from a Texture2D

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Texture | UTexture2D *  |  |  |
| Width | int32  | When less than or equal to zero, the Width of the brush will default to the Width of the Texture |  |
| Height | int32 | When less than or equal to zero, the Height of the brush will default to the Height of the Texture |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSlateBrush  | A new slate brush using the texture. |  |

### MakeBrushFromMaterial

Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
	  is required to hint slate with how large the image wants to be by default.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Material | UMaterialInterface *  |  |  |
| Width | int32  |  |  |
| Height | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSlateBrush  | A new slate brush using the material. |  |

### GetBrushResource

Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### GetBrushResourceConst

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UObject *  |  |  |

### GetBrushResourceAsTexture2D

Gets the brush resource as a texture 2D.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UTexture2D *  |  |  |

### GetBrushResourceAsMaterial

Gets the brush resource as a material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInterface *  |  |  |

### SetBrushResourceToTexture

Sets the resource on a brush to be a UTexture2D.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush &  |  |  |
| Texture | UTexture2D * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetBrushResourceToMaterial

Sets the resource on a brush to be a Material.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush &  |  |  |
| Material | UMaterialInterface * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### NoResourceBrush

Creates a Slate Brush that wont draw anything, the "Null Brush".

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FSlateBrush | A new slate brush that wont draw anything. |  |

### GetDynamicMaterial

Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it, 
	  if it does it will automatically be converted to a MID.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Brush | FSlateBrush & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UMaterialInstanceDynamic *  | A material that supports dynamic input from the game. |  |

### DismissAllMenus

Closes any popup menu

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetAllWidgetsOfClass

Find all widgets of a certain class.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| FoundWidgets | TArray < UUserWidget * > &  | The widgets that were found matching the filter. |  |
| WidgetClass | TSubclassOf < UUserWidget >  | The widget class to filter by. |  |
| TopLevelOnly | bool | Only the widgets that are direct children of the viewport will be returned. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAllWidgetsWithInterface

Find all widgets in the world with the specified interface.
	 This is a slow operation, use with caution e.g. do not use every frame.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| Interface | TSubclassOf < UInterface >  | The interface to find. Must be specified or result array will be empty. |  |
| FoundWidgets | TArray < UUserWidget * > &  | Output array of widgets that implement the specified interface. |  |
| TopLevelOnly | bool | Only the widgets that are direct children of the viewport will be returned. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetInputEventFromKeyEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Event | FKeyEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FInputEvent  |  |  |

### GetKeyEventFromAnalogInputEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Event | FAnalogInputEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FKeyEvent  |  |  |

### GetInputEventFromCharacterEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Event | FCharacterEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FInputEvent  |  |  |

### GetInputEventFromPointerEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Event | FPointerEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FInputEvent  |  |  |

### GetInputEventFromNavigationEvent

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Event | FNavigationEvent & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FInputEvent  |  |  |

### GetSafeZonePadding

Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| SafePadding | FVector2D &  |  |  |
| SafePaddingScale | FVector2D &  |  |  |
| SpillOverPadding | FVector2D & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetHardwareCursor

Loads or sets a hardware cursor from the content directory in the game.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| WorldContextObject | UObject *  |  |  |
| CursorShape | EMouseCursor :: Type  |  |  |
| CursorName | FName  |  |  |
| HotSpot | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### ApplyUserWidgetSkin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UserWidget | UUserWidget *  |  |  |
| SkinPathPtr | TSoftClassPtr < UUserWidgetSkin >  |  |  |
| bAsyncLoad | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### RevertUserWidgetSkin

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| UserWidget | UUserWidget *  |  |  |
| SkinPathPtr | TSoftClassPtr < UUserWidgetSkin > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |
