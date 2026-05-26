# FCollisionImpactData

- Symbol Type: struct
- Symbol Path: FCollisionImpactData
- Source JSON Path: cppstruct/detail/FCollisionImpactData.json
- Source JSON URL: https://developer.gp.qq.com/api/cppstruct/detail/FCollisionImpactData.json
- Mirrored At (UTC): 2026-05-19 08:24:37Z

---

## Description

Information about an overall collision, including contacts.

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ContactInfos | TArray < FRigidBodyContactInfo > | all the contact points in the collision |  |
| TotalNormalImpulse | FVector | the total impulse applied as the two objects push against each other |  |
| TotalFrictionImpulse | FVector | the total counterimpulse applied of the two objects sliding against each other |  |
