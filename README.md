# 株式会社sunrise ホームページ

公開アドレス: https://sasurainoebitiri-code.github.io/-sunrise/
（GitHub Pages。`main` ブランチの直下にあるファイルがそのまま公開されます）

## フォルダの見かた

| 場所 | 中身 |
|---|---|
| `site-src/` | サイトの元データ。`src/site.html`（デザイン・トップ・サービスページ）、`extra.py`（対応エリア・FAQ・コラム記事）、`build.py`（ページを組み立てる）、画像 |
| 直下の `*.html`, `assets/`, `img/`, `column/`, `sitemap.xml` など | `publish.sh` が作る公開用ファイル。**直接編集しない** |
| `redirect-cloudflare/` | 旧アドレス sunrise-kaitai.pages.dev → 新アドレスへの転送用 zip |
| `ops/seo-log.md` | 毎日のSEOチェックの記録 |

## 更新のしかた

1. `site-src/extra.py` や `site-src/src/site.html` を編集
2. `./publish.sh` を実行（ビルド → リンク・構造化データの検査 → 直下へ反映）
3. `main` に commit / push すると、数分で公開サイトに反映

## 注意

- アドレスの途中にリポジトリ名 `/-sunrise` が入るため、`build.py` の `DOMAIN` から自動でパスの先頭に `/-sunrise` を付けています。
  独自ドメインに移す場合は `DOMAIN` を変えるだけで全ページのパスが切り替わります。
- Search Console の所有者確認コードは `build.py` の `GSC_CODES` に追加します。
- `site-src/check_site.py` がリンク切れ・パスの付け忘れ・構造化データの壊れを検査します（`publish.sh` から自動で実行）。
