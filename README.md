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
| `ops/owner-tasks.md` | 松浦様にお願いしたい作業（Search Console・転送・Googleビジネスプロフィール・独自ドメイン・口コミ）の手順と文面 |
| `ops/monitor.py`, `.github/workflows/site-monitor.yml` | 公開サイトの自動監視（5分ごと）。異常があると Issue「サイト監視: 異常あり」が立ち、直ると自動で閉じる |

## 更新のしかた

1. `site-src/extra.py` や `site-src/src/site.html` を編集
2. `./publish.sh` を実行（ビルド → リンク・構造化データの検査 → 直下へ反映）
3. `main` に commit / push すると、数分で公開サイトに反映

## 注意

- コラム一覧は `/-sunrise/column/`（末尾に / が付く）。GitHub Pages では同じ名前のページとフォルダが並ぶと開けないため、`build.py` の `DIR_INDEX` でフォルダの index.html として書き出しています。

- アドレスの途中にリポジトリ名 `/-sunrise` が入るため、`build.py` の `DOMAIN` から自動でパスの先頭に `/-sunrise` を付けています。
  独自ドメインに移す場合は `DOMAIN` を変えるだけで全ページのパスが切り替わります。
- 会社概要などの未記入項目（`src/site.html` の `<span class="todo">[ …を入力 ]</span>`）は公開ページに出さない。値が決まったら書き換えると表示される。
- 独自ドメインにするときは `build.py` の `DOMAIN` を変えるだけで、CNAME の作成と監視先の切り替えも自動で行われる。
- Search Console の所有者確認コードは `build.py` の `GSC_CODES` に追加します。
- `site-src/check_site.py` がリンク切れ・パスの付け忘れ・構造化データの壊れを検査します（`publish.sh` から自動で実行）。
