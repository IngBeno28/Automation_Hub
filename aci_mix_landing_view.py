import streamlit as st

def show_pro_landing():
    # Add viewport meta tag for proper mobile rendering
    st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @media (max-width: 768px) {
            .container { padding: 1rem !important; }
            .feature-card { padding: 1.5rem !important; margin: 1rem 0 !important; }
            .pricing-container { flex-direction: column !important; gap: 1rem !important; }
            .pricing-card { min-width: 100% !important; margin-bottom: 1rem; }
            h1 { font-size: 1.8rem !important; }
            h2 { font-size: 1.5rem !important; }
            h3 { font-size: 1.3rem !important; }
        }
        body {
            color: #31333F;
            background-color: #FFFFFF;
        }
        @media (prefers-color-scheme: dark) {
            .feature-card, .pricing-card {
                background-color: #1E1E1E !important;
                color: #FFFFFF !important;
                border: 1px solid #333 !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h1 style='text-align:center;'>ACI Concrete Mix Optimizer</h1>
    <p style='text-align:center;'>Stop Guessing Your Concrete Mix. Start Optimizing It.</p>

    <div class='container' style='max-width:960px;margin:auto;padding:2rem;'>

    <div class='feature-card' style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h2>Design accurate, standards-based concrete mix proportions in minutes — no spreadsheets, no confusion, no wasted materials.</h2>
    </div>

    <div class='feature-card' style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>🔍 Built by engineers. Powered by ACI.</h3>
      <ul>
        <li>📐 ACI 211-based mix design</li>
        <li>⚖️ Cement, water, aggregates, admixtures — fully calculated</li>
        <li>🧪 Custom slump, durability, strength class</li>
        <li>📁 PDF exports with branding</li>
        <li>🎯 100% online and instant</li>
      </ul>
    </div>

    <div class='feature-card' style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>Use Cases</h3>
      <ul>
        <li>✔️ Field Engineers & QC Labs</li>
        <li>✔️ Construction Site Trials</li>
        <li>✔️ Grad Students / Research Labs</li>
      </ul>
    </div>

    <div class='feature-card' style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
      <h3>Pricing</h3>
      <div class='pricing-container' style='display:flex;gap:2rem;flex-wrap:wrap;'>
        <div class='pricing-card' style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
          <h4>Free</h4>
          <p>1 design at a time<br>CSV Download</p>
          <strong>Ghs 0</strong>
        </div>
        <div class='pricing-card' style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
          <h4>Pro</h4>
          <p>Unlimited designs<br>PDF Download<br>Custom branding</p>
          <strong>GHS 100 (One-time)</strong><br>
    """, unsafe_allow_html=True) # End of the first static markdown block

    # Initialize session state for email if not already present
    if 'pro_email' not in st.session_state:
        st.session_state.pro_email = ""
    # Initialize session state for paystack_ref_counter
    if 'paystack_ref_counter' not in st.session_state:
        st.session_state.paystack_ref_counter = 0

    # Email input with validation
    email = st.text_input("Enter your email to unlock Pro features (via Paystack):",
                         placeholder="your.email@example.com",
                         key="pro_email_input",
                         value=st.session_state.pro_email)

    # Update session state when email input changes
    st.session_state.pro_email = email

    # Paystack Button Logic
    if st.session_state.pro_email: # Only show Paystack if email is provided
        if "@" in st.session_state.pro_email and "." in st.session_state.pro_email.split("@")[-1]:  # Basic email validation
            # Create a placeholder for the button HTML, Streamlit manages its rerendering
            paystack_button_placeholder = st.empty()

            # Construct the JavaScript dynamically
            # Ensure email is properly escaped for JavaScript string
            js_email = st.session_state.pro_email.replace("'", "\\'").replace('"', '\\"')
            # Increment counter for unique reference on each attempt/rerun
            st.session_state.paystack_ref_counter += 1
            js_ref = f"ACI_{st.session_state.pro_email.replace('@', '_').replace('.', '_')}_{st.session_state.paystack_ref_counter}"

            paystack_html = f"""
            <script src="https://js.paystack.co/v1/inline.js"></script>
            <div id="paystack-button-container" style="margin-top:1rem;"></div>
            <script>
              // Check if the button already exists to prevent re-appending on reruns
              // We use a specific ID for the button itself: 'paystack-pay-button'
              if (!document.getElementById('paystack-pay-button')) {{
                  function payWithPaystack() {{
                      var handler = PaystackPop.setup({{
                          key: 'pk_live_2729231e26ba51d2cfa2735e68593252effe2957',
                          email: '{js_email}', // Use the escaped email here
                          amount: 1000000,
                          currency: 'GHS',
                          ref: '{js_ref}', // Use the generated reference
                          callback: function(response) {{
                              // This will be executed on the client-side
                              alert('Payment successful! Reference: ' + response.reference);
                              // Redirect. Streamlit will re-run but the URL will change.
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
                  btn.id = "paystack-pay-button"; // Add a unique ID to the button
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
                  if (container) {{ // Ensure the container exists before appending
                      container.appendChild(btn);
                  }}
              }}
            </script>
            """
            # Use the placeholder to render the HTML
            paystack_button_placeholder.markdown(paystack_html, unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid email address")

    # Final static markdown block
    st.markdown("""
        <a href='https://enhancedconcretemixdesign.streamlit.app/?access_key=your_super_secret_key' target='_blank' style='display:inline-block; margin-top:1rem;'>🚀 Already paid? Go to Pro Version</a>
        </div>
        <div class='pricing-card' style='background:#e0e0e0;border-radius:6px;padding:1rem;flex:1;min-width:200px;'>
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

    <div class='feature-card' style='background:#fff;padding:2rem;margin:2rem 0;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);'>
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
