# yastyleguide
Yet another styleguide


## Install
#### From gitlab pypi repository:
<details><summary>Create gitlab access token.</summary>

Go to page [gitlab settings](https://gitlab.com/-/profile/personal_access_tokens).
Create gitlab access token with scopes:
- api
- read-api
- read_registry
- write_registry

</details>

Set poetry http-basic authentication by token:
```bash
 poetry config http-basic.yastyleguide <gitlab-access-token-name> <gitlab-access-token>
```
Write to **pyproject.toml**:
```toml
[[tool.poetry.source]]
name = "yastyleguide"
url = "https://gitlab.com/api/v4/projects/31783240/packages/pypi/simple"
secondary = true
```
Install by poetry:
```bash
poetry add yastyleguide -D --source=yastyleguide
```

#### From source:
```bash
git clone https://gitlab.com/ds.team/general/yastyleguide
cd yastyleguide 
poetry build
pip install dist/yastyleguide-0.0.3.tar.gz
```

#### From [dist](https://gitlab.com/ds.team/general/yastyleguide/-/jobs/1845796021/artifacts/download) release:
```bash
unzip artifacts.zip
pip install dist/yastyleguide-0.0.3.tar.gz
```

#### From [git](it+https://gitlab.com/ds.team/general/yastyleguide):
```bash
poetry add git+https://gitlab.com/ds.team/general/yastyleguide
```
<details><summary>Публичный вариант</summary>

```bash
poetry add git+https://github.com/levkovalenko/yastyleguide
```
</details>

## Nitpick styleguide

You can use base settings for linters with [nitpick](https://github.com/andreoliwa/nitpick):
```toml
[tool.nitpick]
style = "https://gitlab.com/ds.team/general/yastyleguide/-/blob/master/styles/nitpick-yastyle.toml"
```
<details><summary>Публичный вариант</summary>

```toml
[tool.nitpick]
style = "https://raw.githubusercontent.com/levkovalenko/yastyleguide/master/styles/nitpick-yastyle.toml"
```
</details>

## Running
It's just plugin **flake8**, so:
```bash
flake8 .
```

## Violations
Our own codes:
|Code|Description|
|----|-----------|
|YASG101|`Don't use any 'for' loops.`|
|YASG102|`Don't use any 'while' loops.`|
|YASG201|`Line is to complex, {0} > {1}. To many ast nodes per line.`|
|YASG202|`To big median line complexity in module, {0} > {1}.`|
|YASG203|`To many lines per module, {0} > {1}.`|
|YASG204|`To many function definitions per module, {0} > {1}.`|
|YASG205|`To many class definitions per module, {0} > {1}.`|

You can read about external plugins violations at [/docs/eng/plugin_list.md](docs/eng/plugin_list.md)