import streamlit as st

def show_pro_landing():
    st.markdown("""
    <h1 style='text-align:center;'>ACI Concrete Mix Optimizer</h1>
    <p style='text-align:center;'>Stop Guessing Your Concrete Mix. Start Optimizing It.</p>

    <div style='max-width:960px;margin:auto;padding:2rem;'>

    <div style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h2>Design accurate, standards-based concrete mix proportions in minutes — no spreadsheets, no confusion, no wasted materials.</h2>
    </div>

    <div style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba://cdn.example.com/0,0,0,0.1);'>
      <h3>🔍 Built by engineers. Powered by ACI.</h3>
      <ul>
        <li>📐 ACI 211-based mix design</li>
        <li>⚖️ Cement, water, aggregates, admixtures — fully calculated</li>
        <li>🧪 Custom slump, durability, strength class</li>
        <li>📁 PDF exports with branding</li>
        <li>🎯 100% online and instant</li>
      </ul>
    </div>

    <div style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>Use Cases</h3>
      <ul>
        <li>✔️ Field Engineers & QC Labs</li>
        <li>✔️ Construction Site Trials</li>
        <li>✔️ Grad Students / Research Labs</li>
      </ul>
    </div>

    <div style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>Pricing</h3>
      <div style='display:flex;gap:2rem;flex-wrap:wrap;'>
        <div style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
          <h4>Free</h4>
          <p>1 design at a time<br>CSV Download</p>
          <strong>Ghs 0</strong>
        </div>
        <div style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
          <h4>Pro</h4>
          <p>Unlimited designs<br>PDF Download<br>Custom branding</p>
          <strong>GHS 100 (One-time)</strong><br>
    """, unsafe_allow_html=True)

    # Initialize session state for email if not already present
    if 'pro_email' not in st.session_state:
        st.session_state.pro_email = ""

    # Email input with validation
    # Use key to make sure the widget's state is correctly managed by Streamlit
    email = st.text_input("Enter your email to unlock Pro features (via Paystack):",
                         placeholder="your.email@example.com",
                         key="pro_email_input",
                         value=st.session_state.pro_email) # Set initial value from session state

    # Update session state when email input changes
    st.session_state.pro_email = email

    if st.session_state.pro_email: # Use session state for logic
        if "@" in st.session_state.pro_email and "." in st.session_state.pro_email.split("@")[-1]:  # Basic email validation
            # Only render the JS if it hasn't been rendered yet or if conditions change
            # We'll use a unique key for the markdown to prevent re-execution conflicts
            # Or, more robustly, ensure the container div is uniquely identified and reliably present
            paystack_html = f"""
            <script src="https://js.paystack.co/v1/inline.js"></script>
            <div id="paystack-button-container" style="margin-top:1rem;"></div>
            <script>
              // Check if the button already exists to prevent re-appending on reruns
              if (!document.getElementById('paystack-pay-button')) {{
                  function payWithPaystack() {{
                      var handler = PaystackPop.setup({{
                          key: 'pk_live_2729231e26ba51d2cfa2735e68593252effe2957',
                          email: '{st.session_state.pro_email}', // Use session state email
                          amount: 1000000,
                          currency: 'GHS',
                          ref: 'ACI_' + Math.floor((Math.random() * 1000000000) + 1),
                          callback: function(response) {{
                              alert('Payment successful! Reference: ' + response.reference);
                              // Redirect to pro version after payment
                              window.location.href = 'https://enhancedconcretemixdesign.streamlit.app/?access_key=' + response.reference;
                          }},
                          onClose: function() {{
                              alert('You can complete this payment later. Window closed.');
                          }}
                      }});
                      handler.openIframe();
                  }}

                  // Create and style the button
                  var btn = document.createElement("button");
                  btn.innerHTML = "Pay GHS 100";
                  btn.id = "paystack-pay-button"; // Add an ID to the button for checking its existence
                  btn.style.padding = "12px 25px";
                  btn.style.backgroundColor = "#0aa83f";
                  btn.style.color = "white";
                  btn.style.fontSize = "16px";
                  btn.style.border = "none";
                  btn.style.borderRadius = "8px";
                  btn.style.cursor = "pointer";
                  btn.style.transition = "all 0.3s ease";
                  btn.onmouseenter = function() {{ this.style.opacity = "0.8"; }};
                  btn.onmouseleave = function() {{ this.style.opacity = "1"; }};
                  btn.onclick = payWithPaystack;

                  // Add the button to the container
                  var container = document.getElementById("paystack-button-container");
                  if (container) {{ // Check if container exists before appending
                      container.appendChild(btn);
                  }}
              }}
            </script>
            """
            st.markdown(paystack_html, unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid email address")

    st.markdown("""
        <a href='https://enhancedconcretemixdesign.streamlit.app/?access_key=your_super_secret_key' target='_blank' style='display:inline-block; margin-top:1rem;'>🚀 Already paid? Go to Pro Version</a>
        </div>
        <div style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
          <h4>Institution</h4>
          <p>LMS-ready version<br>Multi-user access<br>Training documents</p>
          <strong>Contact Us</strong><br>
          <a href='mailto:wiafe1713@gmail.com?subject=Institution%20Plan%20Request' style='text-decoration:none;'>📩 Request Quote</a>
        </div>
      </div>
    </div>

    <div style='margin-top:2rem;'>
      <a href='https://Concreteoptimizationtool.streamlit.app' target='_blank' style='display:inline-block; padding:0.5rem 1rem; background:#f0f0f0; border-radius:4px; text-decoration:none;'>👉 Start Designing for Free</a><br>
      <a href='/sample-report.pdf' target='_blank' style='display:inline-block; margin-top:0.5rem; text-decoration:none;'>📄 View Sample PDF Report</a>
    </div>

    <div style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>What You'll Save</h3>
      <ul>
        <li>⏱️ Hours of Excel formula headaches</li>
        <li>💸 Unnecessary cement & aggregate waste</li>
        <li>🤦‍♂️ Errors in hand-calculated mixes</li>
        <li>😤 Time lost to manual recalculations</li>
      </ul>
    </div>

    </div>
    <footer style='text-align:center;padding:1rem;font-size:0.9rem;color:#777;margin-top:2rem;'>
      🧱 ACI Concrete Mix Optimizer | Built by a Civil Engineer, for Civil Engineers
    </footer>
    """, unsafe_allow_html=True)
