# UProceduralFoliageTile

- Symbol Type: class
- Symbol Path: Others / UProceduralFoliageTile
- Source JSON Path: class/detail/Others/UProceduralFoliageTile.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageTile.json
- Mirrored At (UTC): 2026-05-19 08:23:39Z

---

## Description

Procedurally determines where to spawn foliage meshes within a discrete area.
 	Generally, a procedural foliage simulation as a whole is composed of multiple tiles.
 	Tiles are able to overlap one another as well to create a seamless appearance.
 	
 	Note that the tile is not responsible for actually spawning any instances, it only determines where they should be placed.
 	Following a simulation, call ExtractDesiredInstances for information about where each instance should spawn.
 	
 	Note also that, barring any core changes to the ordering of TSet, foliage generation is deterministic 
 	(i.e. given the same inputs, the result of the simulation will always be the same).

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| FoliageSpawner | UProceduralFoliageSpawner * |  |  |
| InstancesArray | TArray < FProceduralFoliageInstance > |  |  |
