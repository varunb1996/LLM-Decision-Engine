# 🧠 LLM Decision Engine (OpenRouter)

A lightweight AI system that simulates fine-tuning using structured prompts and curated examples, built with OpenRouter’s NVIDIA Nemotron model.

---

## 📌 Overview

This project demonstrates how to guide an LLM to produce **structured, senior-level reasoning** without actual model training.

Instead of fine-tuning weights, it uses:
- Prompt templates  
- Few-shot examples  
- Controlled output format  

---

## ⚙️ Model

- OpenRouter API  
- NVIDIA Nemotron 3 Super 120B A12B (free)

---

## 🎯 Features

- Structured outputs:
  - Context  
  - Options  
  - Trade-offs  
  - Recommendation  
  - Failure cases  

- Works on both known and unseen questions  
- No GPU or local training required  

---

## 📂 Structure

llm-decision-engine/ ├── data/ ├── prompts/ ├── src/ ├── .env └── requirements.txt

---

## 🛠️ Setup

```bash
pip install -r requirements.txt

Create .env:

Bash
OPENROUTER_API_KEY=your_api_key

Run:

Bash
cd src
python main.py
