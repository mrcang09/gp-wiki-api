# TagLogFormatPrint

- Symbol Type: globalfunc
- Symbol Path: TagLogFormatPrint
- Source JSON Path: globalfunc/detail/TagLogFormatPrint.json
- Source JSON URL: https://developer.gp.qq.com/api/globalfunc/detail/TagLogFormatPrint.json
- Mirrored At (UTC): 2026-05-19 08:24:50Z

---

## Description

输出格式化的日志，
有三种使用方式，1.原始日志字符串，2.格式化字符串和参数，3.日志类别和日志详细级别、格式、参数。默认日志类别："LogTagLog"，默认详细级别：Log。
生效范围：服务器&客户端

## Parameters

| Name | Type | Description | Redirect |
| --- | --- | --- | --- |
| ... | any | 输入参数 格式1 string log；格式2 string format, vararg params；格式3 string category, ELogVerbosity verbosity, string format, vararg params |  |
