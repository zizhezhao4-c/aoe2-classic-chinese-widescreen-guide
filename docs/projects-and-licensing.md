# 相关项目与许可核对

以下为 2026-10-10 联网核对时的历史快照，不表示当前最新版本或维护状态。使用或贡献前，请打开项目页面重新核对；本教程只引用第三方项目，不附带其二进制或补丁实现。

| 项目 | 许可 | 维护/贡献情况 | 与本案例的关系 |
| --- | --- | --- | --- |
| [withmorten/aoe2wide](https://github.com/withmorten/aoe2wide) | 未找到 LICENSE 或 SPDX 声明 | 历史镜像，最后推送于 2017 年，无 GitHub Release | 原生尺寸和界面处理参考；精确匹配本案例单一构建 |
| [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator) | LGPL-3.0；README 另列 MS-PL 组件 | 已归档，最新发布 2.5.0.1（2021） | 32 位程序中文代码页模拟 |
| [xupefei/Locale-Emulator-Core](https://github.com/xupefei/Locale-Emulator-Core) | 根级自动识别 GPL-3.0；README 明确三个运行库源码目录采用 LGPL-3.0 | 已归档，无独立 Release | 底层语言模拟；许可应按文件/目录分别核对 |
| [FunkyFr3sh/cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) | MIT | 活跃，已核对发行 7.1.0.0；常规 Issues/PR | DirectDraw 兼容，负责输出而非内部视野 |
| [narzoul/DDrawCompat](https://github.com/narzoul/DDrawCompat) | 0BSD | 已核对发行 0.7.1（prerelease）；CONTRIBUTING 明确不接受 PR，接受 Issues | 本案例未采用的兼容层 |

许可原文：

- [Locale Emulator README](https://github.com/xupefei/Locale-Emulator/blob/master/README.md)
- [Locale Emulator Core README](https://github.com/xupefei/Locale-Emulator-Core/blob/master/README.md)
- [cnc-ddraw LICENSE](https://github.com/FunkyFr3sh/cnc-ddraw/blob/master/LICENSE)
- [DDrawCompat LICENSE](https://github.com/narzoul/DDrawCompat/blob/master/LICENSE.txt)
- [DDrawCompat CONTRIBUTING](https://github.com/narzoul/DDrawCompat/blob/master/CONTRIBUTING.md)

## 为什么先分享教程

源码公开与开源许可是两个不同事实。[GitHub 的许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)指出：没有许可证时默认版权保留；公开仓库的查看和 fork 权利不等于一般的再分发或派生作品许可。

本地宽屏生成器参照、翻译或剪裁了 AoE2Wide 的历史代码。取得明确许可前，不将它、旧 patch 表或 sanitized C# 作为我们原创的 MIT 代码公开。公开草稿只包含原创说明、配置和独立编写的只读指纹工具。

## 可选分享路线

1. 新建组合教程仓库：集中保存版本指纹、中文环境、显示兼容和实测结果，引用现有项目。
2. 向适当上游贡献文档：先确认其贡献规则，再决定是否提交具体 PR 或 Issue。
3. 取得 AoE2Wide 权利人明确许可后，再考虑发布衍生生成工具，并标明原作者、改动和原许可。

本教程不代表已向上游提交 Issue/PR、联系作者或取得额外的再发布授权。
