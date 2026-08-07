// ==========================================
// Credit Card Fraud Detection Dashboard
// script.js
// ==========================================


// ==========================================
// Accordion
// ==========================================

function toggleAccordion() {

    const content = document.getElementById("advancedFeatures");
    const arrow = document.getElementById("arrow");

    if (!content) return;

    content.classList.toggle("show");

    if (arrow) {
        arrow.classList.toggle("rotate");
    }

}


// ==========================================
// Demo Legitimate Transaction
// ==========================================

function fillLegitimate() {

    const values = {

        Time: -1.996583,
        Amount: -0.353229,

        V1:-1.359807,
        V2:-0.072781,
        V3:2.536347,
        V4:1.378155,
        V5:-0.338321,
        V6:0.462388,
        V7:0.239599,
        V8:0.098698,
        V9:0.363787,
        V10:0.090794,
        V11:-0.551600,
        V12:-0.617801,
        V13:-0.991390,
        V14:-0.311169,
        V15:1.468177,
        V16:-0.470401,
        V17:0.207971,
        V18:0.025791,
        V19:0.403993,
        V20:0.251412,
        V21:-0.018307,
        V22:0.277838,
        V23:-0.110474,
        V24:0.066928,
        V25:0.128539,
        V26:-0.189115,
        V27:0.133558,
        V28:-0.021053

    };

    fillValues(values);

}


// ==========================================
// Demo Fraud Transaction
// ==========================================

function fillFraud() {

    const values = {

        Time:-1.990000,
        Amount:1.250000,

        V1:-2.312227,
        V2:1.951992,
        V3:-1.609851,
        V4:3.997906,
        V5:-0.522188,
        V6:-1.426545,
        V7:-2.537387,
        V8:1.391657,
        V9:-2.770089,
        V10:-2.772272,
        V11:3.202033,
        V12:-2.899907,
        V13:-0.595222,
        V14:-4.289254,
        V15:0.389724,
        V16:-1.140747,
        V17:-2.830056,
        V18:-0.016822,
        V19:0.416956,
        V20:0.126911,
        V21:0.517232,
        V22:-0.035049,
        V23:-0.465211,
        V24:0.320198,
        V25:0.044519,
        V26:0.177840,
        V27:0.261145,
        V28:-0.143276

    };

    fillValues(values);

}


// ==========================================
// Fill Inputs
// ==========================================

function fillValues(values){

    for(const key in values){

        const input=document.getElementById(key);

        if(input){

            input.value=values[key];

        }

    }

    // Automatically open Advanced Features
    const content=document.getElementById("advancedFeatures");

    const arrow=document.getElementById("arrow");

    if(content && !content.classList.contains("show")){

        content.classList.add("show");

    }

    if(arrow){

        arrow.classList.add("rotate");

    }

}


// ==========================================
// Reset Form
// ==========================================

function resetForm(){

    document.querySelector("form").reset();

    const content=document.getElementById("advancedFeatures");

    const arrow=document.getElementById("arrow");

    if(content){

        content.classList.remove("show");

    }

    if(arrow){

        arrow.classList.remove("rotate");

    }

}


// ==========================================
// Loading Button
// ==========================================

document.addEventListener("DOMContentLoaded",function(){

    const form=document.querySelector("form");

    const button=document.querySelector(".predict-btn");

    if(form && button){

        form.addEventListener("submit",function(){

            button.innerHTML=`
                <i class="fa-solid fa-spinner fa-spin"></i>
                Predicting...
            `;

            button.disabled=true;

        });

    }

});


// ==========================================
// Highlight Selected Model
// ==========================================

document.addEventListener("DOMContentLoaded",function(){

    const radios=document.querySelectorAll('input[name="model"]');

    radios.forEach(function(radio){

        radio.addEventListener("change",function(){

            document.querySelectorAll(".model-card div").forEach(card=>{

                card.classList.remove("selected-model");

            });

            this.nextElementSibling.classList.add("selected-model");

        });

    });

});


// ==========================================
// Console
// ==========================================

console.log("Dashboard Loaded Successfully");