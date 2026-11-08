

# **Cryptocurrency Exchange Simulator — Project Plan**



## 1. Project Overview


**A brief introduction to the project.**

**This project is an educational cryptocurrency spot exchange simulator designed to demonstrate backend development, financial transaction management, order matching, and communication between services written in different programming languages.**

**The system allows users to simulate cryptocurrency trading without using real money or interacting with real blockchain networks.**


## 2. Project Objectives


**The main objectives are:**

- **Build a well-structured REST API using Django REST Framework.**

- **Develop a separate matching-engine service using Rust.**

- **Understand how independent services communicate.**

- **Implement market and limit orders.**

- **Learn how cryptocurrency exchanges manage wallets and transactions.**

- **Implement a double-entry accounting ledger.**

- **Practice database transactions, concurrency control, and idempotency.**

- **Improve software testing and documentation skills.**



## 3. Project Scope


### Included Features

- **User registration and authentication.**

- **Cryptocurrency assets and trading pairs.**

- **Simulated deposits and withdrawals.**

- **User wallets and balance management.**

- **Available and locked balances.**

- **Market and limit orders.**

- **Order matching and partial execution.**

- **Trade history.**

- **Trading fees.**

- **External cryptocurrency market prices.**

- **Basic market data API.**

- **Order cancellation.**

### Excluded Features

- **Real cryptocurrency deposits and withdrawals.**

- **Real financial transactions.**

- **Blockchain integration.**

- **Futures and margin trading.**

- **Leverage and liquidation.**

- **Real-money payment processing.**


## 4. Technology Stack


| Component | Technology |
| :-: | :-: |
| Main backend | Python |
| REST API | Django REST Framework |
| Matching engine | Rust |
| Rust HTTP framework | Axum |
| Main database | PostgreSQL |
| Cache | Redis (later phase) |
| Background tasks | Celery (later phase) |
| Real-time communication | WebSockets (later phase) |
| Testing | pytest, Django Test Framework, Rust tests |
| Containerization | Docker |
| Version control | Git and GitHub |

## 5. System Architecture


**The project consists of two independent applications.**

### Django Backend

**Responsible for:**

- **User management and authentication.**

- **Wallets and balances.**

- **Ledger and financial records.**

- **Order and trade persistence.**

- **Trade settlement and fees.**

- **Public REST API.**

- **External market data integration.**


### Rust Matching Engine


**Responsible for:**

- **Maintaining order books.**

- **Processing incoming orders.**

- **Matching buy and sell orders.**

- **Applying price-time priority.**

- **Handling partial fills.**

- **Returning execution results.**


### Communication



**Django communicates with the Rust matching engine through an internal HTTP API.**

**PostgreSQL is the permanent source of truth for financial records.**


## 6. Development Roadmap


### Phase 1 — Django Foundation

- **Project setup.**

- **Custom user model.**

- **Authentication.**

- **Asset and trading-pair models.**

### Phase 2 — Wallet and Ledger

- **Wallet implementation.**

- **Double-entry ledger.**

- **Simulated deposits and withdrawals.**

- **Database transaction handling.**


### Phase 3 — Rust Fundamentals and Matching Engine

- **Rust fundamentals.**

- **Order and trade data structures.**

- **Order-book implementation.**

- **Matching algorithm.**

- **Unit testing.**


### Phase 4 — Rust HTTP Service

- **Axum setup.**

- **Internal API endpoints.**

- **Request and response handling.**

- **Django-to-Rust communication.**

### Phase 5 — Trading Integration

- **Order submission.**

- **Order cancellation.**

- **Partial execution.**

- **Trade settlement.**

- **Fee calculation.**

- **Failure recovery and idempotency.**


### Phase 6 — Market Data

- **External price provider integration.**

- **Latest market prices.**

- **Redis caching.**

- **Background price updates.**

- **WebSocket updates.**

### Phase 7 — Testing and Reliability

- **Integration testing.**

- **Concurrency testing.**

- **Duplicate request handling.**

- **Crash recovery.**

- **Database consistency checks.**

### Phase 8 — Deployment and Documentation

- **Docker configuration.**

- **CI pipeline.**

- **API documentation.**

- **Architecture diagrams.**

- **Final README and project demonstration.**

