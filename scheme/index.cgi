#!/lisp/bin/gosh

(use wiliki)
(use wiliki.page)
(use wiliki.rss)
(use link-r6rs)
(rss-item-description 'html)

;;---------------------------------------------------------------
;; $$r6rs
;;
(define-reader-macro (r6rs n)
  (let ((url (get-url-r6rs n)))
    `((a (@ (href ,url)) ,n))))

;;---------------------------------------------------------------
;; $$srfi
;;
(define-reader-macro (srfi n)
  (let ((url #`"http://srfi.schemers.org/srfi-,|n|/srfi-,|n|.html") (name #`"SRFI-,n"))
    `((a (@ (href ,url)) ,name))))


(define (page-footer page opts)
  (if (ref page 'mtime)
      `((hr)
        (div (@ (id "footer") (align right))
             "Last modified : "
             ,(wiliki:format-time (ref page 'mtime))
             (br)
             (a (@ (rel "license")
                   (href "http://creativecommons.org/licenses/by/2.1/jp/"))
                (img (@ (alt "Creative Commons License") 
                        (style "border-width:0")
                        (src "http://i.creativecommons.org/l/by/2.1/jp/80x15.png"))))
             (br)
             (a (@ (href "http://shibuya.lisp-users.org/")) "Shibuya.lisp")
             " [" (a (@ (href "/common-lisp/")) "Common Lisp Tips") "]"
             " [" (a (@ (href "/scheme/")) "Scheme Tips") "]"
             (br)
             (a (@ (href "http://clojure-users.org")) "clojure-users.org")
             " [" (a (@ (href "http://rd.clojure-users.org/")) "Clojure Tips") "]"
             (br)
             "Powered by "
             (a (@ (href "http://practical-scheme.net/wiliki/wiliki.cgi")) "WiLiKi") " " ,(wiliki:version) " / "
             (a (@ (href "http://practical-scheme.net/gauche/")) "Gauche") " " ,(gauche-version)
             ))
      '()))

(define-class <fmt> (<wiliki-formatter>)
  ((footer  :init-value page-footer)))

(wiliki:formatter (make <fmt>))


;; google analyticsをheadに仕込む。
;; FIXME: 本来なら、(ref page 'extra-head-elements)に入れておけば良い気がするけど、
;;        方法が分からない --g000001
(define-method wiliki:format-head-elements ((fmt  <fmt>)
                                            (page <wiliki-page>)
                                            . options)
  (append
   ((ref fmt 'head-elements) page options)
   (ref page 'extra-head-elements)
   (list `(script (@ (type "text/javascript"))
                  "
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33070207-2']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
"))))

(define (main args)
  (wiliki-main
    (make <wiliki>
      :db-path "/var/www/tips.lisp-users.org/WiLiKi/wiliki-scheme-tips.dbm"
      :log-file "wiliki-scheme-tips.log"
      :top-page "逆引きScheme"
      :title "逆引きScheme"
      :description "逆引きScheme"
      :style-sheet "wiliki.css"
      :language 'jp
      :charsets '((jp . utf-8) (en . utf-8))
      :image-urls '((#/^http:\/\/tips.lisp-users.org\// allow))
      :gettext-paths '("/var/www/tips.lisp-users.org/Gauche-0.8.14/share/locale/")
      )))
