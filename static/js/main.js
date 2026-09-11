/* =========================================================
   ATIKES GLOBAL INTERACTIONS
========================================================= */

document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       HEADER
    ===================================================== */

    const header =
        document.querySelector(".site-header");

    const updateHeader = () => {

        if (!header) {
            return;
        }

        header.classList.toggle(
            "is-scrolled",
            window.scrollY > 20
        );
    };

    updateHeader();

    window.addEventListener(
        "scroll",
        updateHeader,
        { passive: true }
    );


    /* =====================================================
       SCROLL REVEAL
    ===================================================== */

    const revealElements =
        document.querySelectorAll(
            ".section, .feature-card, .process-card, .service-tile, .scenario-card, .story-card, .outcome-box, .info-card, .faq-card, .case-fact, .case-metric, .case-outcome, .audience-card"
        );

    revealElements.forEach((element, index) => {

        if (
            !element.classList.contains("reveal")
        ) {
            element.classList.add("reveal");
        }

        const delay =
            index % 5 + 1;

        element.dataset.delay =
            delay;
    });


    const observer =
        new IntersectionObserver(
            (entries) => {

                entries.forEach((entry) => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add(
                            "visible"
                        );

                        observer.unobserve(
                            entry.target
                        );
                    }

                });

            },
            {
                threshold: 0.12
            }
        );


    document
        .querySelectorAll(".reveal")
        .forEach((element) => {
            observer.observe(element);
        });


    /* =====================================================
       SMOOTH HASH LINKS
    ===================================================== */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach((link) => {

            link.addEventListener(
                "click",
                function (event) {

                    const id =
                        this.getAttribute("href");

                    if (!id || id === "#") {
                        return;
                    }

                    const target =
                        document.querySelector(id);

                    if (!target) {
                        return;
                    }

                    event.preventDefault();

                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                }
            );

        });


    /* =====================================================
       FAQ
    ===================================================== */

    document
        .querySelectorAll(".faq-question")
        .forEach((question) => {

            question.addEventListener(
                "click",
                function () {

                    const answer =
                        this.nextElementSibling;

                    if (!answer) {
                        return;
                    }

                    const isOpen =
                        answer.classList.contains("open");


                    /* Close all */
                    document
                        .querySelectorAll(".faq-answer.open")
                        .forEach((item) => {
                            item.classList.remove("open");
                        });

                    document
                        .querySelectorAll(".faq-question.open")
                        .forEach((item) => {
                            item.classList.remove("open");
                        });


                    /* Open selected */
                    if (!isOpen) {

                        answer.classList.add(
                            "open"
                        );

                        this.classList.add(
                            "open"
                        );
                    }

                }
            );

        });


    /* =====================================================
       CARD POINTER EFFECT
    ===================================================== */

    document
        .querySelectorAll(
            ".feature-card, .service-tile, .story-card"
        )
        .forEach((card) => {

            card.addEventListener(
                "pointermove",
                (event) => {

                    const rect =
                        card.getBoundingClientRect();

                    const x =
                        event.clientX -
                        rect.left;

                    const y =
                        event.clientY -
                        rect.top;

                    const rotateX =
                        ((y / rect.height) - .5) * -3;

                    const rotateY =
                        ((x / rect.width) - .5) * 3;

                    card.style.transform =
                        `translateY(-8px)
                         perspective(800px)
                         rotateX(${rotateX}deg)
                         rotateY(${rotateY}deg)`;

                }
            );


            card.addEventListener(
                "pointerleave",
                () => {

                    card.style.transform = "";

                }
            );

        });


    /* =====================================================
       BUTTON RIPPLE
    ===================================================== */

    document
        .querySelectorAll(".btn")
        .forEach((button) => {

            button.addEventListener(
                "click",
                function (event) {

                    const ripple =
                        document.createElement("span");

                    ripple.className =
                        "button-ripple";

                    const rect =
                        this.getBoundingClientRect();

                    ripple.style.left =
                        `${event.clientX - rect.left}px`;

                    ripple.style.top =
                        `${event.clientY - rect.top}px`;

                    this.appendChild(ripple);

                    setTimeout(() => {
                        ripple.remove();
                    }, 600);

                }
            );

        });


    /* =====================================================
       MOBILE NAVBAR
    ===================================================== */

    document
        .querySelectorAll("#mainNav .nav-link")
        .forEach((link) => {

            link.addEventListener(
                "click",
                function () {

                    const nav =
                        document.querySelector(
                            "#mainNav"
                        );

                    if (
                        !nav ||
                        !window.bootstrap
                    ) {
                        return;
                    }

                    const collapse =
                        bootstrap.Collapse
                            .getInstance(nav);

                    if (collapse) {
                        collapse.hide();
                    }

                }
            );

        });

});