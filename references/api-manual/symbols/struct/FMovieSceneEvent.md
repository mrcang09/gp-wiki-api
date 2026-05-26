# FMovieSceneEvent

- Symbol Type: struct
- Symbol Path: FMovieSceneEvent
- Source JSON Path: cppstruct/detail/FMovieSceneEvent.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvent.json
- Mirrored At (UTC): 2026-05-19 08:24:43Z

---

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| Ptrs | FMovieSceneEventPtrs | The function that should be called to invoke this event.<br>	 Functions must have either no parameters, or a single, pass-by-value objectinterface parameter, with no return parameter. |  |
| PayloadVariables | TMap < FName , FMovieSceneEventPayloadVariable > | Array of payload variables to be added to the generated function |  |
| CompiledFunctionName | FName |  |  |
| BoundObjectPinName | FName |  |  |
| WeakEndpoint | TWeakObjectPtr < UObject > | Serialized weak pointer to the function entry (UK2Node_FunctionEntry) or custom event node (UK2Node_CustomEvent) within the blueprint graph for this event. Stored as an editor-only UObject so UHT can parse it when building for non-editor. |  |
| GraphGuid_DEPRECATED | FGuid | (deprecated) The UEdGraph::GraphGuid property that relates the graph within which our endpoint lives. |  |
| NodeGuid_DEPRECATED | FGuid | (deprecated) When valid, relates to the The UEdGraphNode::NodeGuid for a custom event node that defines our event endpoint. When invalid, we must be bound to a UBlueprint::FunctionGraphs graph. |  |
| FunctionEntry_DEPRECATED | TWeakObjectPtr < UObject > | Deprecated weak pointer to the function entry to call - no longer serialized but cached on load. Predates GraphGuid and NodeGuid |  |
