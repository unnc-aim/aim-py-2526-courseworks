# AIM Python 2526 Courseworks

UNNC-AIM 国庆 Python 考核作业

## 背景知识

### **Python** 工程相关

这块内容是我们之前课上没有提到的，主要是为了让你了解 Python 工程的一些基本概念。

如果在一个文件夹下有一个 `__init__.py` 文件，那么这个文件夹就被视为一个 **Python 包**（ `Package` ）。包可以包含多个**模块**（ `Module` ），模块是包含 Python 代码的文件。通过包和模块的组织方式，可以**更好地管理和复用代码**。

当你使用 `import` 语句导入一个包时，Python 会执行该包中的 `__init__.py` 文件。这个文件**可以包含初始化代码，也可以定义包的公共接口**（例如，指定哪些模块或子包可以被外部访问）。

### **Git / GitHub** 相关

`Git` 是一个分布式版本控制系统，用于跟踪文件的更改，特别是代码文件。GitHub 是一个基于 Git 的代码托管平台，提供了协作开发、代码审查、问题跟踪等功能。

一般来说，GitHub 上的代码仓库（`Repository`）可以包含多个分支（`Branch`），其中 `main` 分支通常是主要的分支。我们可以创建其他分支（例如 `develop`）来进行开发工作，完成后再将其合并回 `main` 分支。

> 更早的时候，`master` 分支是主要分支的默认名称，但现在很多项目已经改用 `main` 作为主要分支的名称。

完成代码编写和本地测试后，你可以 `Commit` 并 `Push` 到你的 `GitHub` 仓库。每一次提交后，`GitHub Actions` 会按照设定的流程自动在云端运行测试用例，确保你的代码正确无误。

你可以参考的资料：

- [Python 官方文档 - 模块和包](https://docs.python.org/zh-cn/3/tutorial/modules.html#packages)
- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 官方文档](https://docs.github.com/en/get-started/quickstart)
- [GitHub Actions 官方文档](https://docs.github.com/en/actions)

## 🗒️ 你的任务

1. 点击 GitHub 页面右上角的 `Use this template` 按钮，以这个仓库为模板创建你自己的代码仓库
2. 将你自己的仓库克隆到本地，然后在本地创建一个新分支 `develop`，并切换到该分支
3. 在 `develop` 分支上进行代码编写，在 `src/main/` 中补全代码，完成 `TODO` 注释中的任务
4. 在本地使用 pytest 运行测试用例，确保代码正确无误。VS Code 中也可以使用 Testing 功能运行测试用例
5. 如果你在本地测试通过了，记得保存/格式化代码（确保安装了 `ms-python.autopep8` 插件以自动格式化代码）
6. 将代码提交并推送到你自己 `GitHub` 仓库的 `develop` 分支
7. 检查你的 `GitHub` 仓库，确保代码已经成功推送，然后检查自己的代码是否通过了 GitHub Actions 的自动化测试
8. 在 `GitHub` 页面上创建一个 `Pull Request`，将 `develop` 分支合并到你自己仓库的 `main` 分支，合并后再次检查自动化测试是否通过。
9. 自动化通过后，你就可以在 `Actions` 的 `Summary` 页面中找到如何上传这一次的作业到我们问卷的说明 (不通过也可显示，你也可以交上来，但是你的打分会低，谨慎)

## ⚠️ 注意以下事项

- 建议使用 `Python 3.8` 或更高版本编写代码。我们跑测试时使用的应该是 `3.13`，所以建议你在本地使用 `3.8` 以上的版本调试
- 你只能在 `src/main/` 文件夹中补全现有的 `__init__.py` 文件或者添加py代码文件（也需要在 `__init__.py` 中被调用到），**禁止在其他位置修改/添加文件**，否则自动化测试会失败
- 你需要按照 `TODO` 注释中指定的位置编写代码，注意函数命名和缩进的要求，否则 Test 会失败
- 请确保安装了 `ms-python.autopep8` 插件以自动格式化代码，未格式化就提交代码会导致自动化测试失败
- 在代码中你只能使用 Python 标准库，禁止使用任何第三方库
- 你可以在 `VS Code` 中使用本地 `Testing` 功能运行测试用例，确保代码正确，当然也可以多次在 `develop` 分支上不断尝试提交代码/在 `GitHub` 中查看测试结果，直到测试通过
- 我们在评分时也会检查你的代码风格，请确保符合 `PEP8` 规范，以及注意 `Git` 使用相关规范也在考量范围内
