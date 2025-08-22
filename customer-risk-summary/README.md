# 🛡️ KYC Agent: Automate verification, risk profiling, and monitoring with Agentic AI
An intelligent, autonomous KYC Agent equipped with purpose-built tools such as identity verification, document extraction, customer profiling, and risk scoring can transform this process.


🔍 Check KYC requirements

📑 Customer Risk Assessment

🧠 Monitor Customer
---

## ⚙️ Create Agent using Orchestrate ADK

### 1. Install Python 3.11+

Make sure Python 3.11 or above (up to 3.13) is installed.

### 2. Clone the Repository

```bash
git@github.com:esantan-ibm/agentic-ai-bootcamp.git
```

### 3. Navigate into the project

```bash
cd customer-risk-summary
```

### 4. Create a Virtual Environment

```bash
python -m venv envadk
```

### 5. Install ADK and Validate

```bash
pip install ibm-watsonx-orchestrate

orchestrate --version
orchestrate --help
```

### 6. Add Watsonx Environment

```bash
orchestrate env add -n <name> -u <service-instance-url>
```

### 7. Activate Environment

```bash
orchestrate env activate <name>
# You will be prompted to enter the WXO API key
```
### 8. Create `.env` File at fsm-agentic-ai-bootcamp/customer-risk-summary/tools (Not Required for present tools, but for future tools that require credentials)

Create a `.env` file with the following (if you are using any credentials in any custom tools):

```env
COS_ENDPOINT =
COS_API_KEY_ID =
COS_INSTANCE_CRN =
COS_BUCKET_NAME =
API_KEY =
PROJECT_ID =
IBM_CLOUD_URL =
```

### 9. Import Tools & Agents

```bash

pip install -r requirements.txt

./import-all.sh
```

### 10. Test on Orchestrate UI

Ask questions like:

* Show me the pending KYC applications for review

* Start review for Ryan Hogan's application

* Show the KYC requirements summary for this customer

* Why is the risk level of this customer high?

* Show the risk profile summary for customer id - cust001

* Review the recent transactions for this customer

---

## 🧪 Optional - Create Agent using Orchestrate ADK Developer Edition

### 1. Install Docker

### Install Docker + Docker Compose to run Orchestrate locally using containers.

brew install docker

brew install docker-compose

### Install colima

brew install colima

colima start --cpu-type host --arch host --vm-type=vz --mount-type virtiofs -c 8 -m 16


### 2. Get IBM Entitlement Key

* Go to [My IBM](https://myibm.ibm.com/products-services/containerlibrary)
* Click **View Library** > **Add a new key +**
* Copy your **Entitlement Key**

### 3. Create `.env` File at KYC_Compliance/orchestrate_adk_lab/

Create a `.env` file with the following:

```env
WO_DEVELOPER_EDITION_SOURCE=myibm
WO_ENTITLEMENT_KEY=your-entitlement-key
WO_INSTANCE=your-instance-url
WO_API_KEY=your-WO-api-key
```

### 4. Start Orchestrate Server

```bash
orchestrate server start --env-file=.env
```

### 5. Activate Local Environment

```bash
orchestrate env activate local
```       

### 6. Import Tools & Agents


```bash
./import-all.sh
```

### 7. Start Orchestrate Chat UI

```bash
orchestrate chat start
```

Try asking:

* Show me the pending KYC applications for review

* Start review for Ryan Hogan's application

* Show the KYC requirements summary for this customer

* Why is the risk level of this customer high?

* Show the risk profile summary for customer id - cust001

* Review the recent transactions for this customer

### 8. View Server Logs

```bash
orchestrate server logs
```

---


## 🧠 Summary

This project showcases how AI Agents built using IBM Watsonx Orchestrate can simplify Customer Risk Assessment.
