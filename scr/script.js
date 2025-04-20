document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("pre > code").forEach((codeBlock) => {
      const pre = codeBlock.parentNode;
  
      const button = document.createElement("button");
      button.innerText = "Copy";
      button.className = "copy-button";
  
      const wrapper = document.createElement("div");
      wrapper.style.position = "relative";
  
      pre.parentNode.insertBefore(wrapper, pre);
      wrapper.appendChild(pre);
      wrapper.appendChild(button);
  
      button.addEventListener("click", () => {
        const text = codeBlock.innerText;
  
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(() => {
            showCopied(button);
          }).catch((err) => {
            fallbackCopy(text, button);
          });
        } else {
          fallbackCopy(text, button);
        }
      });
  
      function fallbackCopy(text, button) {
        const textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        try {
          document.execCommand("copy");
          showCopied(button);
        } catch (err) {
          console.error("Fallback copy failed", err);
          button.innerText = "Error";
        }
        document.body.removeChild(textarea);
      }
  
      function showCopied(button) {
        button.classList.add("copied");
        button.innerText = "Copied!";
        setTimeout(() => {
          button.innerText = "Copy";
          button.classList.remove("copied");
        }, 2000);
      }
    });
  });