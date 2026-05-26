# CommodityOperationManager

- Symbol Type: class
- Symbol Path: 和平全局接口 / 商业化与功能模板 / CommodityOperationManager
- Source JSON Path: class/detail/和平全局接口/商业化与功能模板/CommodityOperationManager.json
- Source JSON URL: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/CommodityOperationManager.json
- Mirrored At (UTC): 2026-05-19 08:23:22Z

---

## Description

UGC商业化购买流程全局管理器

## Variables

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| CommodityOperationManager.BuyProductResultDelegate |  | 生效范围：客户端&&服务端<br>发起购买商品后触发<br>@param Result BuyProductResult @购买结果 |  |
| CommodityOperationManager.LimitProductUpdateDelegate |  | 生效范围：客户端&&服务端<br>限购商品购买次数发生变化时触发 |  |
| CommodityOperationManager.PurchasedProductListUpdateDelegate |  | 生效范围：客户端&&服务端<br>商品购买次数发生变化时触发 |  |

## Functions

### BuyProduct

发起商品购买
生效范围：客户端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProductID | number | 商品的ID |  |
| Num | number | 购买商品数量 |  |
| CurrentPrice | number | 发起购买时的价格，用于校验 |  |
| bCheckPrivilege | boolean | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | PromiseFuture | 绿洲币购买UI界面的PromiseFuture实例，非绿洲币商品则返回nil |  |

### ServerBuyProduct

发起自定义货币商品购买
生效范围：服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerKey | number | 发起购买者的 PlayerKey |  |
| ProductID | number | 商品的ID |  |
| Num | number | 购买商品数量 |  |
| CurrentPrice | number | 发起购买时的价格，用于校验 |  |
| bCheckPrivilege | boolean | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |  |

### CanAfford

检查是否买得起指定数量的商品
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProductID | number | 商品的ID |  |
| Num | number | 购买的商品数量 |  |
| PlayerController | UUGCPlayerController | 玩家控制器，客户端可以不传 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | boolean |  |  |

### GetLimitPurchasedTimes

获得限购商品的购买次数
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProductID | number | 商品的ID |  |
| PlayerController | UUGCPlayerController | 玩家控制器，客户端可以不传 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetAllLimitPurchasedProducts

获取所有已购买的限购商品
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | UUGCPlayerController | 玩家控制器，客户端可以不传 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### GetPurchasedTimes

获得商品的累计购买次数
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProductID | number | 商品的ID |  |
| PlayerController | UUGCPlayerController | 玩家控制器，客户端可以不传 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | number |  |  |

### GetAllPurchasedProducts

获取所有已购买的商品
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| PlayerController | UUGCPlayerController | 玩家控制器，客户端可以不传 |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### GetAllProductData

获取所有商品信息
生效范围：客户端&&服务器

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |

### GetProductData

获取指定商品信息
生效范围：客户端&&服务端

Parameters:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ProductID | number | 商品的ID |  |

Returns:

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
|  | table |  |  |
