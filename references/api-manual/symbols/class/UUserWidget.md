# UUserWidget

- Symbol Type: class
- Symbol Path: Others / UUserWidget
- Source JSON Path: class/detail/Others/UUserWidget.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UUserWidget.json
- Mirrored At (UTC): 2026-05-19 08:23:41Z

---

## Description

The user widget is extensible by users through the WidgetBlueprint.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ColorAndOpacity | FLinearColor | The color and opacity of this widget.  Tints all child widgets. |  |
| ColorAndOpacityDelegate | FGetLinearColor |  |  |
| ForegroundColor | FSlateColor | The foreground color of the widget, this is inherited by sub widgets.  Any color property<br>	  that is marked as inherit will use this color. |  |
| ForegroundColorDelegate | FGetSlateColor |  |  |
| Padding | FMargin | The padding area around the content. |  |
| ActiveSequencePlayers | TArray < UUMGSequencePlayer * > | All the sequence players currently playing |  |
| StoppedSequencePlayers | TArray < UUMGSequencePlayer * > | List of sequence players to cache and clean up when safe |  |
| NamedSlotBindings | TArray < FNamedSlotBinding > | Stores the widgets being assigned to named slots |  |
| WidgetTree | UWidgetTree * | The widget tree contained inside this user widget initialized by the blueprint |  |
| bOptimiseAnimation | bool |  |  |
| bNoBubbleUpEvent | bool |  |  |
| Priority | int32 |  |  |
| bSupportsKeyboardFocus_DEPRECATED | uint8 |  |  |
| bIsFocusable | uint8 | Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to. |  |
| bStopAction | uint8 |  |  |
| CanDisableDrag | uint8 |  |  |
| bCanEverTick | uint8 | If a widget doesn't ever need to tick the blueprint, setting this to false is an optimization. |  |
| bCanEverPaint | uint8 | If a widget doesn't ever need to do custom painting in the blueprint, setting this to false is an optimization. |  |
| bCookedWidgetTree | uint8 | If this user widget was created using a cooked widget tree.  If that's true, we want to skip a lot of the normal<br>	  initialization logic for widgets, because these widgets have already been initialized. |  |
| WidgetSkinProxy | UObject * | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "WidgetSkin") |  |
| InputComponent | UInputComponent * |  |  |
| AnimationCallbacks | TArray < FAnimationEventBinding > |  |  |

## Functions

### AddToViewport

Adds it to the game's viewport and fills the entire screen, unless SetDesiredSizeInViewport is called
	  to explicitly set the size.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ZOrder | int32 | The higher the number, the more on top this widget will be. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### AddToPlayerScreen

Adds the widget to the game's viewport in a section dedicated to the player.  This is valuable in a split screen
	  game where you need to only show a widget over a player's portion of the viewport.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ZOrder | int32 | The higher the number, the more on top this widget will be. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### RemoveFromViewport

Removes the widget from the viewport.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetZOrderOfViewportWidget

Get Z-order of Viewport Widget, added by fourthchen

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int |  |  |

### SetPositionInViewport

Sets the widgets position in the viewport.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Position | FVector2D  | The 2D position to set the widget to in the viewport. |  |
| bRemoveDPIScale | bool | If you've already calculated inverse DPI, set this to false. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetDesiredSizeInViewport

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Size | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetOffsetsInViewport

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Margin | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAnchorsInViewport

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Anchors | FAnchors |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetAlignmentInViewport

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Alignment | FVector2D |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetAnchorsInViewport

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FAnchors |  |  |

### GetAlignmentInViewport

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FVector2D |  |  |

### GetIsVisible

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### IsInViewport

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | true if the widget was added to the viewport using AddToViewport. |  |

### GetOwningLocalPlayer

Gets the local player associated with this UI.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | ULocalPlayer * | The owning local player. |  |

### SetOwningLocalPlayer

Sets the player associated with this UI via LocalPlayer reference.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LocalPlayer | ULocalPlayer * | The local player you want to be the conceptual owner of this UI. |  |

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

### SetOwningPlayer

Sets the local player associated with this UI via PlayerController reference.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| LocalPlayerController | APlayerController * | The PlayerController of the local player you want to be the conceptual owner of this UI. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetOwningPlayerPawn

Gets the player pawn associated with this UI.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | APawn * | Gets the owning player pawn that's owned by the player controller assigned to this widget. |  |

### PreConstruct

Called by both the game and the editor.  Allows users to run initial setup for their widgets to better preview
	  the setup in the designer and since generally that same setup code is required at runtime, it's called there
	  as well.
	 
	  WARNING
	  This is intended purely for cosmetic updates using locally owned data, you can not safely access any game related
	  state, if you call something that doesn't expect to be run at editor time, you may crash the editor.
	 
	  In the event you save the asset with blueprint code that causes a crash on evaluation.  You can turn off
	  PreConstruct evaluation in the Widget Designer settings in the Editor Preferences.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| IsDesignTime | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### Construct

Called after the underlying slate widget is constructed.  Depending on how the slate object is used
	  this event may be called multiple times due to adding and removing from the hierarchy.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### ConstructForLua

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Destruct

Called when a widget is no longer referenced causing the slate resource to destroyed.  Just like
	  Construct this event can be called multiple times.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### Tick

Ticks this widget.  Override in derived classes, but always call the parent implementation.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The space allotted for this widget |  |
| InDeltaTime | float | Real time passed since last tick |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnPaint

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Context | FPaintContext & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsInteractable

Gets a value indicating if the widget is interactive.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### OnFocusReceived

Called when keyboard focus is given to this widget.  This event does not bubble.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InFocusEvent | FFocusEvent | FocusEvent |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnFocusLost

Called when this widget loses focus.  This event does not bubble.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFocusEvent | FFocusEvent | FocusEvent |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnAddedToFocusPath

If focus is gained on on this widget or on a child widget and this widget is added
	  to the focus path, and wasn't previously part of it, this event is called.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFocusEvent | FFocusEvent | FocusEvent |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnRemovedFromFocusPath

If focus is lost on on this widget or on a child widget and this widget is
	  no longer part of the focus path.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InFocusEvent | FFocusEvent | FocusEvent |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnKeyChar

Called after a character is entered while this widget has focus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InCharacterEvent | FCharacterEvent | Character event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnPreviewKeyDown

Called after a key (keyboard, controller, ...) is pressed when this widget or a child of this widget has focus
	  If a widget handles this event, OnKeyDown will not be passed to the focused widget.
	 
	  This event is primarily to allow parent widgets to consume an event before a child widget processes
	  it and it should be used only when there is no better design alternative.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InKeyEvent | FKeyEvent | Key event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnKeyDown

Called after a key (keyboard, controller, ...) is pressed when this widget has focus (this event bubbles if not handled)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InKeyEvent | FKeyEvent | Key event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnKeyUp

Called after a key (keyboard, controller, ...) is released when this widget has focus

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InKeyEvent | FKeyEvent | Key event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnAnalogValueChanged

Called when an analog value changes on a button that supports analog

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| InAnalogInputEvent | FAnalogInputEvent | Analog Event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnMouseButtonDown

The system calls this method to notify the widget that a mouse button was pressed within it. This event is bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  | Whether the event was handled along with possible requests for the system to take action. |  |

### OnPreviewMouseButtonDown

Just like OnMouseButtonDown, but tunnels instead of bubbling.
	  If this even is handled, OnMouseButtonDown will not be sent.
	  
	  Use this event sparingly as preview events generally make UIs more
	  difficult to reason about.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  | Whether the event was handled along with possible requests for the system to take action. |  |

### OnMouseButtonUp

The system calls this method to notify the widget that a mouse button was release within it. This event is bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  | Whether the event was handled along with possible requests for the system to take action. |  |

### OnMouseMove

The system calls this method to notify the widget that a mouse moved within it. This event is bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  | Whether the event was handled along with possible requests for the system to take action. |  |

### OnMouseEnter

The system will use this event to notify a widget that the cursor has entered it. This event is NOT bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  | The Geometry of the widget receiving the event |  |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnMouseLeave

The system will use this event to notify a widget that the cursor has left it. This event is NOT bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MouseEvent | FPointerEvent & | Information about the input event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnMouseWheel

Called when the mouse wheel is spun. This event is bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  |  |
| MouseEvent | FPointerEvent & | Mouse event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnMouseButtonDoubleClick

Called when a mouse button is double clicked.  Override this in derived classes.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InMyGeometry | FGeometry  | Widget geometry |  |
| InMouseEvent | FPointerEvent & | Mouse button event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnDragDetected

Called when Slate detects that a widget started to be dragged.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  |  |
| PointerEvent | FPointerEvent &  | MouseMove that triggered the drag |  |
| Operation | UDragDropOperation * & |   The drag operation that was detected. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnDragCancelled

Called when the user cancels the drag operation, typically when they simply release the mouse button after
	  beginning a drag operation, but failing to complete the drag.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent &  | Last mouse event from when the drag was canceled. |  |
| Operation | UDragDropOperation * |   The drag operation that was canceled. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnDragEnter

Called during drag and drop when the drag enters the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |   The geometry of the widget receiving the event. |  |
| PointerEvent | FPointerEvent  |  The mouse event from when the drag entered the widget. |  |
| Operation | UDragDropOperation * |   The drag operation that entered the widget. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnDragLeave

Called during drag and drop when the drag leaves the widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PointerEvent | FPointerEvent  |  The mouse event from when the drag left the widget. |  |
| Operation | UDragDropOperation * |   The drag operation that entered the widget. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnDragOver

Called during drag and drop when the the mouse is being dragged over a widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |   The geometry of the widget receiving the event. |  |
| PointerEvent | FPointerEvent  |  The mouse event from when the drag occurred over the widget. |  |
| Operation | UDragDropOperation * |   The drag operation over the widget. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 'true' to indicate that you handled the drag over operation.  Returning 'false' will cause the operation to continue to bubble up. |  |

### OnDrop

Called when the user is dropping something onto a widget.  Ends the drag and drop operation, even if no widget handles this.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |   The geometry of the widget receiving the event. |  |
| PointerEvent | FPointerEvent  |  The mouse event from when the drag occurred over the widget. |  |
| Operation | UDragDropOperation * |   The drag operation over the widget. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | 'true' to indicate you handled the drop operation. |  |

### OnTouchGesture

Called when the user performs a gesture on trackpad. This event is bubbled.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |   The geometry of the widget receiving the event. |  |
| GestureEvent | FPointerEvent & | gesture event |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  Returns whether the event was handled, along with other possible actions |  |

### OnTouchStarted

Called when a touchpad touch is started (finger down)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  The geometry of the widget receiving the event. |  |
| InTouchEvent | FPointerEvent & | The touch event generated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### OnTouchMoved

Called when a touchpad touch is moved  (finger moved)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  The geometry of the widget receiving the event. |  |
| InTouchEvent | FPointerEvent & | The touch event generated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### OnTouchEnded

Called when a touchpad touch is ended (finger lifted)

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  The geometry of the widget receiving the event. |  |
| InTouchEvent | FPointerEvent & | The touch event generated |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### OnMotionDetected

Called when motion is detected (controller or device)
	  e.g. Someone tilts or shakes their controller.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| MyGeometry | FGeometry  |  The geometry of the widget receiving the event. |  |
| InMotionEvent | FMotionEvent |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | FEventReply  |  |  |

### OnMouseCaptureLost

Called when mouse capture is lost if it was owned by this widget.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### GetAllChildrenOfType

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Type | FString  |  |  |
| Children | TArray < UWidget * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetTypedChildrenOfWidget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Parent | UWidget *  |  |  |
| Type | FString  |  |  |
| Children | TArray < UWidget * > & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindToAnimationStarted

Bind an animation started delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation *  | the animation to listen for starting or finishing. |  |
| Delegate | FWidgetAnimationDynamicEvent | the delegate to call when the animation's state changes |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindFromAnimationStarted

Unbind an animation started delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation *  | the animation to listen for starting or finishing. |  |
| Delegate | FWidgetAnimationDynamicEvent | the delegate to call when the animation's state changes |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindAllFromAnimationStarted

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindToAnimationFinished

Bind an animation finished delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation *  | the animation to listen for starting or finishing. |  |
| Delegate | FWidgetAnimationDynamicEvent | the delegate to call when the animation's state changes |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindFromAnimationFinished

Unbind an animation finished delegate.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation *  | the animation to listen for starting or finishing. |  |
| Delegate | FWidgetAnimationDynamicEvent | the delegate to call when the animation's state changes |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### UnbindAllFromAnimationFinished

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### BindToAnimationEvent

Allows binding to a specific animation's event.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation *  | the animation to listen for starting or finishing. |  |
| Delegate | FWidgetAnimationDynamicEvent  | the delegate to call when the animation's state changes |  |
| AnimationEvent | EWidgetAnimationEvent  | the event to watch for. |  |
| UserTag | FName | Scopes the delegate to only be called when the animation completes with a specific tag set on it when it was played. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnAnimationStarted

Called when an animation is started.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation * | the animation that started |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### OnAnimationFinished

Called when an animation has either played all the way through or is stopped

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Animation | UWidgetAnimation * | The animation that has finished playing |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetColorAndOpacity

Sets the tint of the widget, this affects all child widgets.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InColorAndOpacity | FLinearColor | The tint to apply to all child widgets. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetForegroundColor

Sets the foreground color of the widget, this is inherited by sub widgets.  Any color property 
	  that is marked as inherit will use this color.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InForegroundColor | FSlateColor | The foreground color. |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPadding

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InPadding | FMargin |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayAnimation

Plays an animation in this widget a specified number of times

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation *  | The animation to play |  |
| StartAtTime | float  | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |  |
| NumLoopsToPlay | int32  | The number of times to loop this animation (0 to loop indefinitely) |  |
| PlayMode | EUMGSequencePlayMode :: Type  | Specifies the playback mode |  |
| PlaybackSpeed | float | The speed at which the animation should play |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PlayAnimationTo

Plays an animation in this widget a specified number of times stoping at a specified time

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation *  | The animation to play |  |
| StartAtTime | float  | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |  |
| EndAtTime | float  | The absolute time in the animation where to stop, this is only considered in the last loop. |  |
| NumLoopsToPlay | int32  | The number of times to loop this animation (0 to loop indefinitely) |  |
| PlayMode | EUMGSequencePlayMode :: Type  | Specifies the playback mode |  |
| PlaybackSpeed | float | The speed at which the animation should play |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopAnimation

Stops an already running animation in this widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### JumpAnimation

Stop and jump to the specified time in this widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation *  | The animation to jump |  |
| JumpAtTime | float | specified time |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### PauseAnimation

Pauses an already running animation in this widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | the time point the animation was at when it was paused, relative to its start position.  Use this as the StartAtTime when you trigger PlayAnimation. |  |

### GetAnimationCurrentTime

Gets the current time of the animation in this widget

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | float  | the current time of the animation. |  |

### IsAnimationPlaying

Gets whether an animation is currently playing on this widget.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * | The animation to check the playback status of |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  | True if the animation is currently playing |  |

### IsAnyAnimationPlaying

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool | True if any animation is currently playing |  |

### SetNumLoopsToPlay

Changes the number of loops to play given a playing animation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation *  | The animation that is already playing |  |
| NumLoopsToPlay | int32 | The number of loops to play. (0 to loop indefinitely) |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetPlaybackSpeed

Changes the playback rate of a playing animation

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation *  | The animation that is already playing |  |
| PlaybackSpeed | float |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### ReverseAnimation

If an animation is playing, this function will reverse the playback.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * | The playing animation that we want to reverse |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### IsAnimationPlayingForward

returns true if the animation is currently playing forward, false otherwise.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| InAnimation | UWidgetAnimation * | The playing animation that we want to know about |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### PlaySound

Plays a sound through the UI

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| SoundToPlay | USoundBase * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### GetWidgetFromName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget *  |  The uobject widget corresponding to a given name |  |

### GetVariableWidgetFromName

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Name | FName & |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UWidget *  |  |  |

### IsPlayingAnimation

Are we currently playing any animations?

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool |  |  |

### NewWidgetObjectBP

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Outer | UObject *  |  |  |
| UserWidgetClass | UClass * |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | UUserWidget *  |  |  |

### GetCacheLayerId

return CacheLayerId only windows

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | int32 |  |  |

### ListenForInputAction

Listens for a particular Player Input Action by name.  This requires that those actions are being executed, and
	  that we're not currently in UI-Only Input Mode.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionName | FName  |  |  |
| EventType | TEnumAsByte < EInputEvent >  |  |  |
| bConsume | bool  |  |  |
| Callback | FOnInputAction |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopListeningForInputAction

Removes the binding for a particular action's callback.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionName | FName  |  |  |
| EventType | TEnumAsByte < EInputEvent > |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### StopListeningForAllInputActions

Stops listening to all input actions, and unregisters the input component with the player controller.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### RegisterInputComponent

ListenForInputAction will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### UnregisterInputComponent

StopListeningForAllInputActions will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void |  |  |

### IsListeningForInputAction

Checks if the action has a registered callback with the input component.

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ActionName | FName |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | bool  |  |  |

### SetInputActionPriority

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| NewPriority | int32 |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |

### SetInputActionBlocking

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| bShouldBlock | bool |  |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | void  |  |  |
