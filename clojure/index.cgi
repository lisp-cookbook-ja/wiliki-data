#!/home/tips_lisp_users/bin/gosh

(use wiliki)

(use wiliki.rss)
(rss-item-description 'html)

(define (main args)
  (wiliki-main
    (make <wiliki>
      :db-path "/home/tips_lisp_users/WiLiKi/wiliki-clojure-tips.dbm"
      :log-file "wiliki-clojure-tips.log"
      :top-page "逆引きClojure"
      :title "逆引きClojure"
      :description "逆引きClojure"
      :style-sheet "cl.css"
      :language 'jp
      :charsets '((jp . utf-8) (en . utf-8))
      :image-urls '((#/^http:\/\/tips.lisp-users.org\// allow))
      :gettext-paths '("/home/tips_lisp_users/Gauche-0.8.14/share/locale/")
      )))
